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
