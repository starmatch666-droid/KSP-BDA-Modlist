// BDArmory 武器/导弹 GetInfo 文本中文
// 这些文本在源码里用字符串插值硬编码，没有 #loc 键；这里在 GetInfo 返回值上做替换。

using System;
using System.Linq;
using System.Reflection;
using HarmonyLib;
using KSP;
using UnityEngine;

namespace BDACNInfo
{
    [KSPAddon(KSPAddon.Startup.Instantly, true)]
    public class Bootstrap : MonoBehaviour
    {
        private static bool _patched;

        public void Awake()
        {
            if (_patched)
                return;
            _patched = true;
            try
            {
                var harmony = new Harmony("com.kisa.bda.cn.info");
                PatchBdaInfo(harmony);
            }
            catch (Exception ex)
            {
                Debug.LogError("[BDA_CN_Info] patch failed: " + ex);
            }
        }

        private static void PatchBdaInfo(Harmony harmony)
        {
            var bda = AssemblyLoader.loadedAssemblies
                .Select(a => a.assembly)
                .FirstOrDefault(a => a.GetName().Name == "BDArmory");
            if (bda == null)
            {
                Debug.LogWarning("[BDA_CN_Info] BDArmory assembly not found.");
                return;
            }

            var postfix = new HarmonyMethod(
                typeof(InfoTextPatch).GetMethod("Postfix", BindingFlags.Static | BindingFlags.NonPublic));
            int patched = 0;
            foreach (var type in bda.GetTypes())
            {
                if (type.Namespace == null || !type.Namespace.StartsWith("BDArmory"))
                    continue;
                var method = type.GetMethod("GetInfo", BindingFlags.Public | BindingFlags.Instance,
                    null, Type.EmptyTypes, null);
                if (method == null || method.DeclaringType != type || method.ReturnType != typeof(string))
                    continue;
                harmony.Patch(method, postfix: postfix);
                patched++;
            }
            Debug.Log("[BDA_CN_Info] Patched BDA GetInfo methods: " + patched);
        }
    }

    internal static class InfoTextPatch
    {
        private static readonly string[,] Replacements =
        {
            { "Weapon Type: ", "武器类型：" },
            { "Rounds Per Minute: ", "每分钟射速：" },
            { "Ammunition: ", "弹药：" },
            { "Max Range: ", "最大射程：" },
            { "Shot Deviation: ", "散布：" },
            { " mrad, 80% hit", " 毫弧度，80% 命中" },
            { "Bullet type: ", "弹丸类型：" },
            { "Bullet mass: ", "弹丸质量：" },
            { "Muzzle velocity: ", "炮口初速：" },
            { "Estimated Penetration: ", "预计穿深：" },
            { "Blast:", "爆炸：" },
            { "- tnt mass: ", "- TNT 当量：" },
            { "- tnt Mass: ", "- TNT 当量：" },
            { " - TNT Mass: ", " - TNT 当量：" },
            { "- fuze type: ", "- 引信类型：" },
            { "- radius: ", "- 半径：" },
            { "Air detonation: True", "空爆：是" },
            { "Air detonation: False", "空爆：否" },
            { "- Air detonation: True", "- 空爆：是" },
            { "- Air detonation: False", "- 空爆：否" },
            { "Guidance: ", "制导：" },
            { "Boresight: ", "离轴角：" },
            { "Remaining: ", "剩余：" },
            { "- max range: ", "- 最大射程：" },
            { "- Estimated Penetration: ", "- 预计穿深：" },
            { "MISSING", "缺失" },
            { "ballistic", "弹道" },
            { "Impact", "撞击" },
            { "Incendiary", "燃烧" },
        };

        private static void Postfix(ref string __result)
        {
            if (string.IsNullOrEmpty(__result))
                return;
            for (int i = 0; i < Replacements.GetLength(0); i++)
                __result = __result.Replace(Replacements[i, 0], Replacements[i, 1]);
        }
    }
}
