using System;
using System.Collections.Generic;
using System.Globalization;
using System.Reflection;
using CommNet;
using UnityEngine;

namespace ScienceLabAutoTransmit
{
    [KSPAddon(KSPAddon.Startup.AllGameScenes, false)]
    public class ScienceLabAutoTransmitAddon : MonoBehaviour
    {
        private const string ConfigNodeName = "SCIENCE_LAB_AUTO_TRANSMIT";
        private const string LogPrefix = "[ScienceLabAutoTransmit] ";

        private static readonly FieldInfo TransmittingField =
            typeof(ModuleScienceLab).GetField(
                "transmittingData",
                BindingFlags.Instance | BindingFlags.NonPublic);

        private readonly Dictionary<int, double> nextRetry =
            new Dictionary<int, double>();
        private readonly HashSet<int> loggedUnloadedProblems =
            new HashSet<int>();

        private float thresholdPercent = 99f;
        private float checkIntervalSeconds = 5f;
        private float retryIntervalSeconds = 20f;
        private bool verboseLogging = true;
        private bool transmitUnloadedLabs = true;
        private double nextScan;

        public void Start()
        {
            LoadSettings();
            Debug.Log(string.Format(
                CultureInfo.InvariantCulture,
                "{0}started; threshold={1:0.##}% check={2:0.##}s retry={3:0.##}s unloaded={4}",
                LogPrefix,
                thresholdPercent,
                checkIntervalSeconds,
                retryIntervalSeconds,
                transmitUnloadedLabs));
        }

        public void Update()
        {
            if (!FlightGlobals.ready)
            {
                return;
            }

            double now = Time.unscaledTime;
            if (now < nextScan)
            {
                return;
            }

            nextScan = now + checkIntervalSeconds;
            List<Vessel> vessels = FlightGlobals.Vessels;
            for (int vesselIndex = 0; vesselIndex < vessels.Count; vesselIndex++)
            {
                Vessel vessel = vessels[vesselIndex];
                if (vessel == null || vessel.isEVA)
                {
                    continue;
                }

                if (!vessel.loaded)
                {
                    if (transmitUnloadedLabs)
                    {
                        TryTransmitUnloadedVessel(vessel, now);
                    }
                    continue;
                }

                if (CommNetScenario.CommNetEnabled
                    && (vessel.connection == null || !vessel.connection.CanScience))
                {
                    continue;
                }

                if (ScienceUtil.GetBestTransmitter(vessel) == null)
                {
                    continue;
                }

                List<Part> parts = vessel.parts;
                for (int partIndex = 0; partIndex < parts.Count; partIndex++)
                {
                    Part part = parts[partIndex];
                    if (part == null)
                    {
                        continue;
                    }

                    for (int moduleIndex = 0; moduleIndex < part.Modules.Count; moduleIndex++)
                    {
                        ModuleScienceLab lab = part.Modules[moduleIndex] as ModuleScienceLab;
                        if (lab == null)
                        {
                            continue;
                        }

                        TryTransmitLab(vessel, part, lab, now);
                    }
                }
            }
        }

        private void TryTransmitUnloadedVessel(Vessel vessel, double now)
        {
            if (ResearchAndDevelopment.Instance == null
                || vessel.protoVessel == null
                || vessel.protoVessel.protoPartSnapshots == null)
            {
                return;
            }

            bool hasTransmitter = HasUnloadedTransmitter(vessel.protoVessel);
            List<ProtoPartSnapshot> parts = vessel.protoVessel.protoPartSnapshots;
            for (int partIndex = 0; partIndex < parts.Count; partIndex++)
            {
                ProtoPartSnapshot part = parts[partIndex];
                if (part == null)
                {
                    continue;
                }

                ProtoPartModuleSnapshot labSnapshot = part.FindModule("ModuleScienceLab");
                if (labSnapshot == null)
                {
                    continue;
                }

                int scienceCap = GetPrefabScienceCap(part);
                if (scienceCap <= 0)
                {
                    continue;
                }

                float storedScience;
                if (!TryReadFloat(labSnapshot.moduleValues, "storedScience", out storedScience))
                {
                    continue;
                }

                float threshold = scienceCap * thresholdPercent / 100f;
                if (storedScience + 0.001f < threshold)
                {
                    continue;
                }

                int labId = part.flightID.GetHashCode();
                if (!hasTransmitter)
                {
                    if (verboseLogging && loggedUnloadedProblems.Add(labId))
                    {
                        Debug.LogWarning(string.Format(
                            CultureInfo.InvariantCulture,
                            "{0}unloaded lab {1} is ready ({2:0.###}/{3}) but no ModuleDataTransmitter was found on {4}",
                            LogPrefix,
                            part.partInfo != null ? part.partInfo.title : part.partName,
                            storedScience,
                            scienceCap,
                            vessel.GetDisplayName()));
                    }
                    continue;
                }

                double retryAt;
                if (nextRetry.TryGetValue(labId, out retryAt) && now < retryAt)
                {
                    continue;
                }

                int scienceToTransmit = Mathf.FloorToInt(storedScience);
                if (scienceToTransmit <= 0)
                {
                    continue;
                }

                nextRetry[labId] = now + retryIntervalSeconds;
                ResearchAndDevelopment.Instance.AddScience(
                    scienceToTransmit,
                    TransactionReasons.ScienceTransmission);
                labSnapshot.moduleValues.SetValue(
                    "storedScience",
                    (storedScience - scienceToTransmit).ToString(
                        "R",
                        CultureInfo.InvariantCulture));

                string message = string.Format(
                    CultureInfo.InvariantCulture,
                    "{0}transmitted {1} science from unloaded lab {2} on {3}",
                    LogPrefix,
                    scienceToTransmit,
                    part.partInfo != null ? part.partInfo.title : part.partName,
                    vessel.GetDisplayName());
                if (verboseLogging)
                {
                    Debug.Log(message);
                }
                ScreenMessages.PostScreenMessage(
                    message,
                    4f,
                    ScreenMessageStyle.UPPER_LEFT);
            }
        }

        private static bool HasUnloadedTransmitter(ProtoVessel protoVessel)
        {
            List<ProtoPartSnapshot> parts = protoVessel.protoPartSnapshots;
            for (int partIndex = 0; partIndex < parts.Count; partIndex++)
            {
                ProtoPartSnapshot part = parts[partIndex];
                if (part == null || part.modules == null)
                {
                    continue;
                }

                List<ProtoPartModuleSnapshot> modules = part.modules;
                for (int moduleIndex = 0; moduleIndex < modules.Count; moduleIndex++)
                {
                    ProtoPartModuleSnapshot module = modules[moduleIndex];
                    if (module == null || module.moduleName == null)
                    {
                        continue;
                    }

                    if (module.moduleName.StartsWith(
                            "ModuleDataTransmitter",
                            StringComparison.Ordinal)
                        || module.moduleName.StartsWith(
                            "ModuleRTAntenna",
                            StringComparison.Ordinal))
                    {
                        return true;
                    }
                }
            }

            return false;
        }

        private static int GetPrefabScienceCap(ProtoPartSnapshot part)
        {
            if (part.partInfo == null || part.partInfo.partPrefab == null)
            {
                return 0;
            }

            PartModuleList modules = part.partInfo.partPrefab.Modules;
            for (int moduleIndex = 0; moduleIndex < modules.Count; moduleIndex++)
            {
                ModuleScienceConverter converter =
                    modules[moduleIndex] as ModuleScienceConverter;
                if (converter != null)
                {
                    return converter.scienceCap;
                }
            }

            return 0;
        }

        private void TryTransmitLab(Vessel vessel, Part part, ModuleScienceLab lab, double now)
        {
            ModuleScienceConverter converter = lab.Converter;
            if (converter == null || converter.scienceCap <= 0)
            {
                return;
            }

            float threshold = converter.scienceCap * thresholdPercent / 100f;
            if (lab.storedScience + 0.001f < threshold)
            {
                return;
            }

            if (TransmittingField != null
                && (bool)TransmittingField.GetValue(lab))
            {
                return;
            }

            int labId = lab.GetInstanceID();
            double retryAt;
            if (nextRetry.TryGetValue(labId, out retryAt) && now < retryAt)
            {
                return;
            }

            float scienceToTransmit = lab.storedScience;
            nextRetry[labId] = now + retryIntervalSeconds;
            lab.TransmitScience();

            if (verboseLogging)
            {
                Debug.Log(string.Format(
                    CultureInfo.InvariantCulture,
                    "{0}queued {1:0.###}/{2} science from {3} ({4}) on {5}",
                    LogPrefix,
                    scienceToTransmit,
                    converter.scienceCap,
                    part.partInfo.title,
                    part.flightID,
                    vessel.GetDisplayName()));
            }
        }

        private void LoadSettings()
        {
            ConfigNode[] nodes = GameDatabase.Instance.GetConfigNodes(ConfigNodeName);
            if (nodes == null || nodes.Length == 0)
            {
                return;
            }

            ConfigNode node = nodes[0];
            thresholdPercent = ReadFloat(node, "thresholdPercent", thresholdPercent);
            checkIntervalSeconds = ReadFloat(
                node,
                "checkIntervalSeconds",
                checkIntervalSeconds);
            retryIntervalSeconds = ReadFloat(
                node,
                "retryIntervalSeconds",
                retryIntervalSeconds);
            verboseLogging = ReadBool(node, "verboseLogging", verboseLogging);
            transmitUnloadedLabs = ReadBool(
                node,
                "transmitUnloadedLabs",
                transmitUnloadedLabs);

            thresholdPercent = Mathf.Clamp(thresholdPercent, 50f, 99.9f);
            checkIntervalSeconds = Mathf.Clamp(checkIntervalSeconds, 1f, 60f);
            retryIntervalSeconds = Mathf.Clamp(retryIntervalSeconds, 5f, 300f);
        }

        private static float ReadFloat(ConfigNode node, string key, float fallback)
        {
            string value = node.GetValue(key);
            float result;
            if (!string.IsNullOrEmpty(value)
                && float.TryParse(
                    value,
                    NumberStyles.Float,
                    CultureInfo.InvariantCulture,
                    out result))
            {
                return result;
            }

            return fallback;
        }

        private static bool TryReadFloat(ConfigNode node, string key, out float value)
        {
            value = 0f;
            string text = node.GetValue(key);
            return !string.IsNullOrEmpty(text)
                && float.TryParse(
                    text,
                    NumberStyles.Float,
                    CultureInfo.InvariantCulture,
                    out value);
        }

        private static bool ReadBool(ConfigNode node, string key, bool fallback)
        {
            string value = node.GetValue(key);
            bool result;
            return !string.IsNullOrEmpty(value) && bool.TryParse(value, out result)
                ? result
                : fallback;
        }
    }
}
