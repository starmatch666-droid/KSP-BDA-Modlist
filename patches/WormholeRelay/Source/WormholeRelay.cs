// ============================================================================
//  WormholeRelay —— 让虫洞两端的"中继卫星"之间能建立通信链路
//  (KSP 1.12.x / 原版 CommNet / 需要 Harmony)
//
//  原理：
//    原版 CommNet 只按"直线距离 + 天线功率"判定连通，没有"隧道"的概念。
//    本插件在 CommNet 建网时挂钩 CommNetwork.TryConnect(a, b, distance, ...)：
//    只要 a、b 两个通信节点分别位于配置里两个虫洞天体的 SOI 内（即"引力范围"），
//    就把这次判定的距离改成一个小值（1000 m）→ 原来的距离/功率判定自然通过，
//    链路与信号强度都由 CommNet 自己算，不碰它的内部结构。
//
//  用法：
//    默认认 Kcalbeloh 的 WH3141A / WH3141B。
//    同一侧的两个中继不会被连（只连 A 侧 ↔ B 侧）。
//    中继的定义：飞船至少有一根 antennaType = RELAY 的 ModuleDataTransmitter。
//
//  配置（可选）：GameData/WormholeRelay/WormholeRelay.cfg
//    WORMHOLE_RELAY
//    {
//        sideA = WH3141A
//        sideB = WH3141B
//        linkDistance = 1000
//    }
// ============================================================================

using System;
using System.Collections.Generic;
using HarmonyLib;
using UnityEngine;
using CommNet;

namespace WormholeRelay
{
    [KSPAddon(KSPAddon.Startup.Flight, false)]
    public class WormholeRelayAddon : MonoBehaviour
    {
        // 节点 → 所在侧（1 = sideA，2 = sideB），每帧刷新
        internal static readonly Dictionary<CommNode, int> NodeSide = new Dictionary<CommNode, int>();

        internal static string SideAName = "WH3141A";
        internal static string SideBName = "WH3141B";
        internal static double LinkDistance = 1000.0;

        private static bool _harmonyDone;
        private int _tick;
        private int _lastCount = -1;

        void Awake()
        {
            LoadConfig();
            if (!_harmonyDone)
            {
                _harmonyDone = true;
                try
                {
                    var h = new Harmony("KISA.WormholeRelay");
                    h.PatchAll(typeof(WormholeRelayAddon).Assembly);
                    Debug.Log("[WormholeRelay] Harmony 补丁已应用；sideA=" + SideAName + " sideB=" + SideBName);
                }
                catch (Exception ex)
                {
                    Debug.LogError("[WormholeRelay] Harmony 打补丁失败: " + ex.Message);
                }
            }
        }

        static void LoadConfig()
        {
            try
            {
                var nodes = GameDatabase.Instance.GetConfigNodes("WORMHOLE_RELAY");
                if (nodes == null || nodes.Length == 0) return;
                var n = nodes[0];
                if (n.HasValue("sideA")) SideAName = n.GetValue("sideA");
                if (n.HasValue("sideB")) SideBName = n.GetValue("sideB");
                if (n.HasValue("linkDistance")) double.TryParse(n.GetValue("linkDistance"), out LinkDistance);
                Debug.Log("[WormholeRelay] 读取配置: sideA=" + SideAName + " sideB=" + SideBName + " linkDistance=" + LinkDistance);
            }
            catch (Exception ex) { Debug.LogWarning("[WormholeRelay] 配置读取失败，用默认值: " + ex.Message); }
        }

        void Update()
        {
            if (++_tick % 15 != 0) return;   // 每 15 帧刷一次即可
            if (!FlightGlobals.ready) return;

            NodeSide.Clear();
            int count = 0;
            foreach (var v in FlightGlobals.Vessels)
            {
                if (v == null || v.mainBody == null) continue;
                if (v.vesselType == VesselType.Debris || v.vesselType == VesselType.EVA ||
                    v.vesselType == VesselType.Flag || v.vesselType == VesselType.SpaceObject) continue;

                int side = SideOf(v.mainBody.bodyName);
                if (side == 0) continue;
                if (!HasRelayAntenna(v)) continue;

                var node = GetNode(v);
                if (node == null) continue;
                NodeSide[node] = side;
                count++;
            }

            // 进出的中继数量变化时，让 CommNet 重建一次网络，链路立刻生效
            if (count != _lastCount)
            {
                _lastCount = count;
                RebuildNetworks();
            }
        }

        internal static int SideOf(string bodyName)
        {
            if (string.IsNullOrEmpty(bodyName)) return 0;
            if (string.Equals(bodyName, SideAName, StringComparison.OrdinalIgnoreCase)) return 1;
            if (string.Equals(bodyName, SideBName, StringComparison.OrdinalIgnoreCase)) return 2;
            return 0;
        }

        internal static bool IsWormholePair(CommNode a, CommNode b, out int sideA, out int sideB)
        {
            sideA = 0; sideB = 0;
            if (a == null || b == null) return false;
            if (!NodeSide.TryGetValue(a, out sideA)) return false;
            if (!NodeSide.TryGetValue(b, out sideB)) return false;
            return sideA != sideB;      // 只连"两端"，同侧不连
        }

        static bool HasRelayAntenna(Vessel v)
        {
            var parts = v.parts;
            if (parts == null) return false;
            for (int i = 0; i < parts.Count; i++)
            {
                var modules = parts[i].Modules;
                if (modules == null) continue;
                for (int j = 0; j < modules.Count; j++)
                {
                    var t = modules[j] as ModuleDataTransmitter;
                    if (t != null && t.antennaType == AntennaType.RELAY) return true;
                }
            }
            return false;
        }

        static CommNode GetNode(Vessel v)
        {
            try
            {
                var cn = v.connection;
                if (cn == null) return null;
                return cn.Comm;
            }
            catch { return null; }
        }

        static void RebuildNetworks()
        {
            var seen = new HashSet<CommNetwork>();
            foreach (var v in FlightGlobals.Vessels)
            {
                var node = GetNode(v);
                if (node == null) continue;
                try
                {
                    var net = node.Net;
                    if (net != null && seen.Add(net)) net.Rebuild();
                }
                catch { }
            }
            if (NodeSide.Count > 0)
                Debug.Log("[WormholeRelay] 当前虫洞侧中继数: " + NodeSide.Count + "，已请求重建通信网络");
        }
    }

    [HarmonyPatch(typeof(CommNetwork), "TryConnect")]
    static class PatchTryConnect
    {
        // 参数名与 KSP 1.12.5 内部方法一致（a, b, distance, aCanRelay, bCanRelay, bothRelay）
        static void Prefix(CommNode a, CommNode b, ref double distance)
        {
            int sa, sb;
            if (WormholeRelayAddon.IsWormholePair(a, b, out sa, out sb))
            {
                distance = WormholeRelayAddon.LinkDistance;
            }
        }
    }
}
