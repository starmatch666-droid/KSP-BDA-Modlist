using System;
using System.Collections.Generic;
using System.Globalization;
using System.Reflection;
using CommNet;
using UnityEngine;

namespace ScienceLabAutoTransmit
{
    [KSPAddon(KSPAddon.Startup.Flight, false)]
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

        private float thresholdPercent = 99f;
        private float checkIntervalSeconds = 5f;
        private float retryIntervalSeconds = 20f;
        private bool verboseLogging = true;
        private double nextScan;

        public void Start()
        {
            LoadSettings();
            Debug.Log(string.Format(
                CultureInfo.InvariantCulture,
                "{0}started; threshold={1:0.##}% check={2:0.##}s retry={3:0.##}s",
                LogPrefix,
                thresholdPercent,
                checkIntervalSeconds,
                retryIntervalSeconds));
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
            List<Vessel> vessels = FlightGlobals.VesselsLoaded;
            for (int vesselIndex = 0; vesselIndex < vessels.Count; vesselIndex++)
            {
                Vessel vessel = vessels[vesselIndex];
                if (vessel == null || !vessel.loaded || vessel.isEVA)
                {
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
