// BDArmory Plus 编辑器分类按钮中文
// BDA 的 bdacategory 字符串同时用于过滤和显示，不能直接改成中文；
// 这里只在 PartCategorizerButton 初始化时把显示名换成 #LOC 键，
// 过滤逻辑仍然使用原来的英文 categoryName。

using System.Collections.Generic;
using HarmonyLib;
using KSP;
using KSP.UI.Screens;
using UnityEngine;

namespace BDACN
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
            var harmony = new Harmony("com.kisa.bda.cn.categories");
            harmony.PatchAll(typeof(Bootstrap).Assembly);
        }
    }

    [HarmonyPatch(typeof(PartCategorizerButton), "InitializeToggleBtn")]
    internal static class InitializeToggleBtnPatch
    {
        private static readonly Dictionary<string, string> Keys =
            new Dictionary<string, string>
            {
                { "All", "#LOC_BDA_CN_Category_All" },
                { "Control", "#LOC_BDA_CN_Category_Control" },
                { "Guns", "#LOC_BDA_CN_Category_Guns" },
                { "Gun turrets", "#LOC_BDA_CN_Category_GunTurrets" },
                { "Lasers", "#LOC_BDA_CN_Category_Lasers" },
                { "Laser turrets", "#LOC_BDA_CN_Category_LaserTurrets" },
                { "Rocket pods", "#LOC_BDA_CN_Category_RocketPods" },
                { "Rocket turrets", "#LOC_BDA_CN_Category_RocketTurrets" },
                { "Missiles", "#LOC_BDA_CN_Category_Missiles" },
                { "Missile turrets", "#LOC_BDA_CN_Category_MissileTurrets" },
                { "Bombs", "#LOC_BDA_CN_Category_Bombs" },
                { "Torpedoes", "#LOC_BDA_CN_Category_Torpedoes" },
                { "Ammo", "#LOC_BDA_CN_Category_Ammo" },
                { "Radars", "#LOC_BDA_CN_Category_Radars" },
                { "Targeting", "#LOC_BDA_CN_Category_Targeting" },
                { "Countermeasures", "#LOC_BDA_CN_Category_Countermeasures" },
                { "Armor", "#LOC_BDA_CN_Category_Armor" },
                { "Misc", "#LOC_BDA_CN_Category_Misc" },
                { "Legacy", "#LOC_BDA_CN_Category_Legacy" },
                { "Armory", "#LOC_BDA_CN_Category_Armory" },
            };

        private static void Prefix(string categoryName, ref string categorydisplayName)
        {
            string key;
            if (categoryName == categorydisplayName && Keys.TryGetValue(categoryName, out key))
                categorydisplayName = key;
        }
    }
}
