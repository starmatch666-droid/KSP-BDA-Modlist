using System;
using HarmonyLib;
using MuMech;
using UnityEngine;

namespace MechJebInfiniteFuel
{
    [KSPAddon(KSPAddon.Startup.Instantly, true)]
    public sealed class MechJebInfiniteFuelAddon : MonoBehaviour
    {
        private static bool _patched;

        private void Awake()
        {
            if (_patched)
            {
                return;
            }

            try
            {
                var harmony = new Harmony("starmatch666-droid.MechJebInfiniteFuel");
                harmony.PatchAll(typeof(MechJebInfiniteFuelAddon).Assembly);
                _patched = true;
                Debug.Log("[MechJebInfiniteFuel] Harmony patch applied.");
            }
            catch (Exception ex)
            {
                Debug.LogError("[MechJebInfiniteFuel] Failed to apply Harmony patch: " + ex);
            }
        }
    }

    [KSPAddon(KSPAddon.Startup.Flight, false)]
    public sealed class MechJebInfiniteFuelWindow : MonoBehaviour
    {
        private const int WindowId = 0x4D4A4946;
        private Rect _window = new Rect(Screen.width - 320f, 80f, 300f, 180f);

        private static MechJebCore FindMechJebCore(Vessel vessel)
        {
            if (vessel == null || vessel.parts == null)
            {
                return null;
            }

            for (int i = 0; i < vessel.parts.Count; i++)
            {
                Part part = vessel.parts[i];
                if (part == null || part.Modules == null)
                {
                    continue;
                }

                for (int j = 0; j < part.Modules.Count; j++)
                {
                    MechJebCore core = part.Modules[j] as MechJebCore;
                    if (core != null)
                    {
                        return core;
                    }
                }
            }

            return null;
        }

        private static string FormatDuration(double seconds)
        {
            long totalSeconds = (long)Math.Round(Math.Abs(seconds));
            long hours = totalSeconds / 3600;
            long minutes = (totalSeconds % 3600) / 60;
            long secs = totalSeconds % 60;
            return string.Format("{0:00}:{1:00}:{2:00}", hours, minutes, secs);
        }

        private void OnGUI()
        {
            if (!CheatOptions.InfinitePropellant ||
                HighLogic.LoadedScene != GameScenes.FLIGHT)
            {
                return;
            }

            Vessel vessel = FlightGlobals.ActiveVessel;
            if (vessel == null || !vessel.loaded || vessel.patchedConicSolver == null)
            {
                return;
            }

            _window = GUILayout.Window(
                WindowId,
                _window,
                DrawWindow,
                "MechJeb Infinite Fuel",
                GUILayout.Width(300f));
        }

        private void DrawWindow(int windowId)
        {
            Vessel vessel = FlightGlobals.ActiveVessel;
            MechJebCore core = FindMechJebCore(vessel);
            if (core == null || core.Node == null)
            {
                GUILayout.Label("MechJeb core not found.");
                GUI.DragWindow();
                return;
            }

            if (vessel.patchedConicSolver.maneuverNodes.Count == 0)
            {
                GUILayout.Label("No maneuver node.");
                GUILayout.Label("Infinite Propellant: ON");
                GUI.DragWindow();
                return;
            }

            ManeuverNode node = vessel.patchedConicSolver.maneuverNodes[0];
            double deltaV = node.GetBurnVector(vessel.orbit).magnitude;
            double acceleration = core.Node.VesselState.limitedMaxThrustAccel;

            if (!(acceleration > 0.000001) ||
                double.IsNaN(acceleration) ||
                double.IsInfinity(acceleration))
            {
                GUILayout.Label("No usable engine acceleration.");
                GUILayout.Label("Node delta-v: " + deltaV.ToString("F2") + " m/s");
                GUI.DragWindow();
                return;
            }

            double burnDuration = deltaV / acceleration;
            double burnStartUt = node.UT - burnDuration * 0.5;
            double burnEndUt = node.UT + burnDuration * 0.5;
            double now = Planetarium.GetUniversalTime();
            double ignitionCountdown = burnStartUt - now;
            double nodeCountdown = node.UT - now;

            GUILayout.Label("Burn duration: " + FormatDuration(burnDuration));
            GUILayout.Label("Ignition UT: " + burnStartUt.ToString("F0"));
            GUILayout.Label("Node UT: " + node.UT.ToString("F0"));
            GUILayout.Space(4f);

            if (now < burnStartUt)
            {
                GUILayout.Label("Ignition T-minus: " + FormatDuration(ignitionCountdown));
            }
            else if (now <= burnEndUt)
            {
                GUILayout.Label("Ignition: BURNING");
                GUILayout.Label("Burn time left: " + FormatDuration(burnEndUt - now));
            }
            else
            {
                GUILayout.Label("Ignition: BURN WINDOW PASSED");
            }

            GUILayout.Label(
                "Node T-minus: " +
                (nodeCountdown >= 0.0 ? "-" : "+") +
                FormatDuration(nodeCountdown));
            GUILayout.Space(4f);
            GUILayout.Label("Node delta-v: " + deltaV.ToString("F2") + " m/s");
            GUILayout.Label("Acceleration: " + acceleration.ToString("F6") + " m/s^2");
            GUI.DragWindow();
        }
    }

    [HarmonyPatch(typeof(MechJebModuleNodeExecutor), "BurnTime")]
    internal static class PatchMechJebNodeExecutorBurnTime
    {
        private static bool _loggedActiveCalculation;

        // BurnTime is private in MechJeb 2.15.x. Replacing it only while KSP's
        // InfinitePropellant cheat is enabled makes the node executor schedule
        // long burns by constant-mass acceleration instead of finite StageStats.
        private static bool Prefix(
            MechJebModuleNodeExecutor __instance,
            double dv,
            out double halfBurnTime,
            out double spoolupTime,
            ref double __result)
        {
            halfBurnTime = 0.0;
            spoolupTime = 0.0;

            if (!CheatOptions.InfinitePropellant)
            {
                return true;
            }

            double acceleration = __instance.VesselState.limitedMaxThrustAccel;
            if (!(acceleration > 0.000001) ||
                double.IsNaN(acceleration) ||
                double.IsInfinity(acceleration) ||
                dv < 0.0 ||
                double.IsNaN(dv) ||
                double.IsInfinity(dv))
            {
                return true;
            }

            double burnTime = dv / acceleration;
            if (!(burnTime > 0.0) ||
                double.IsNaN(burnTime) ||
                double.IsInfinity(burnTime))
            {
                return true;
            }

            halfBurnTime = burnTime * 0.5;
            __result = burnTime;

            if (!_loggedActiveCalculation)
            {
                _loggedActiveCalculation = true;
                Debug.Log(
                    "[MechJebInfiniteFuel] Infinite propellant burn timing enabled: " +
                    "dv=" + dv.ToString("F3") +
                    " m/s, acceleration=" + acceleration.ToString("F6") +
                    " m/s^2, burn=" + burnTime.ToString("F1") + " s.");
            }

            return false;
        }
    }
}
