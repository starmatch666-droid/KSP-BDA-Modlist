using System;
using System.Collections.Generic;
using System.Text.RegularExpressions;
using HarmonyLib;
using KSP;
using KSP.Localization;
using UnityEngine;
using UnityEngine.UI;

namespace GroundConstructionCN
{
    [KSPAddon(KSPAddon.Startup.MainMenu, true)]
    public class Bootstrap : MonoBehaviour
    {
        private static bool _patched;

        public void Awake()
        {
            if (_patched)
                return;

            _patched = true;
            if (Localizer.CurrentLanguage != "zh-cn")
                return;

            var harmony = new Harmony("com.kisa.groundconstruction.cn");
            harmony.PatchAll(typeof(Bootstrap).Assembly);
        }
    }

    [HarmonyPatch(typeof(Text), "set_text")]
    internal static class TextSetterPatch
    {
        private static readonly Dictionary<string, string> Exact =
            new Dictionary<string, string>(StringComparer.Ordinal)
            {
                { "Available DIY kits:", "可用 DIY 套件：" },
                { "Built DIY kits:", "已建造 DIY 套件：" },
                { "Construction Queue", "建造队列" },
                { "DIY Kit: ", "DIY 套件：" },
                { "Kit Cost", "套件成本" },
                { "Kit Mass", "套件质量" },
                { "Kit Crew", "套件乘员" },
                { "Kit Parts", "套件部件" },
                { "Kit Resources", "套件资源" },
                { "Launch", "发射" },
                { "Start Construction", "开始建造" },
                { "Pause Construction", "暂停建造" },
                { "Resume Construction", "继续建造" },
                { "No Operational Workshops", "没有可用工坊" },
                { "No workers in the workshop.", "工坊里没有工人。" },
                { "Press to open Workshop Window", "点击打开工坊窗口" },
                { "Select Vessel", "选择飞船" },
                { "Select crew for the assembled vessel", "为组装好的飞船选择乘员" },
                { "Show Required Resources", "显示所需资源" },
                { "Resources required", "所需资源" },
                { "Transfer resources between the workshop and the assembled vessel", "在工坊与组装好的飞船之间转移资源" },
                { "Workshop Window", "工坊窗口" },
                { "Workshop is idle", "工坊空闲" },
                { "Workshop Efficiency", "工坊效率" },
                { "Cannot deploy construction kit unless landed.", "建造套件只能在着陆状态下展开。" },
                { "Cannot deploy construction kit while moving.", "移动时无法展开建造套件。" },
                { "Cannot deploy construction kit while rotating.", "旋转时无法展开建造套件。" },
                { "Cannot launch constructed ship unless landed.", "建造好的飞船只能在着陆状态下发射。" },
                { "Cannot launch constructed ship while mooving.", "移动时无法发射建造好的飞船。" },
                { "Cannot launch constructed ship while rotating.", "旋转时无法发射建造好的飞船。" },
                { "The workshop can only operate when the vessel is landed", "工坊只能在飞船着陆时运作" },
                { "The workshop can only operate when the vessel is in orbit", "工坊只能在飞船处于轨道时运作" },
                { "Engineers cannot work while the workshop is moving.", "工坊移动时工程师无法工作。" },
                { "Selected container is not suitable for construction of this kit", "所选容器不适合建造这个套件" },
                { "It is possible to construct this kit directly in the assembly space", "可以直接在装配空间里建造这个套件" },
                { "Wield the construct with the construction docking port (if any).", "用建造对接口（如果有）固定这个构造体。" },
                { "Stop construction and move the kit back to the Queue", "停止建造并把套件放回队列" },
                { "Start, Pause or Resume construction", "开始、暂停或继续建造" },
                { "Launch assembled vessel", "发射组装好的飞船" },
                { "Launch after construction", "建造完成后发射" },
                { "Launch orientation:", "发射朝向：" },
                { "Rotate launch direction", "旋转发射方向" },
                { "Switch to this workshop", "切换到这个工坊" },
                { "This is the active vessel", "这是当前飞船" },
                { "Add this kit to construction queue", "把这个套件加入建造队列" },
                { "Discard this kit", "丢弃这个套件" },
                { "Rename Kit", "重命名套件" },
                { "AbortLaunch", "中止发射" },
                { "ASSEMBLED", "已组装" },
                { "CONSTRUCTED", "已建造" },
                { "CONSTRUCTION", "建造中" },
                { "VESSEL_KIT", "飞船套件" },
                { "DIY_KIT", "DIY 套件" },
                { "After construction:", "建造完成后：" },
                { "<b>Kit:</b>", "<b>套件：</b>" },
                { "Launching. Please, wait...", "正在发射，请稍候……" }
            };

        private static readonly List<KeyValuePair<Regex, string>> Patterns =
            new List<KeyValuePair<Regex, string>>
            {
                new KeyValuePair<Regex, string>(
                    new Regex(@"^Construction options for <b>(.*)$"),
                    "建造选项：<b>$1"),
                new KeyValuePair<Regex, string>(
                    new Regex(@"^Additional resources required for <b>(.*?)</b>$"),
                    "建造 <b>$1</b> 还需要额外资源"),
                new KeyValuePair<Regex, string>(
                    new Regex(@"^Requirements: work (.*), energy (.*), amount (.*), mass (.*), resource (.*)$"),
                    "需求：工作量 $1，电力 $2，数量 $3，质量 $4，资源 $5"),
                new KeyValuePair<Regex, string>(
                    new Regex(@"^Engineers at '(.*)' should have completed the work on the '(.*)' by now\.$"),
                    "“$1”的工程师现在应该已经完成“$2”的建造了。"),
                new KeyValuePair<Regex, string>(
                    new Regex(@"^Show workshops on (.*)$"),
                    "显示工坊：$1"),
                new KeyValuePair<Regex, string>(
                    new Regex(@"^<b><color=#FFD100><size=30>Launching\. Please, wait\.\.\.</size></color></b>$"),
                    "<b><color=#FFD100><size=30>正在发射，请稍候……</size></color></b>")
            };

        private static void Prefix(ref string value)
        {
            if (string.IsNullOrEmpty(value))
                return;

            string translated;
            if (Exact.TryGetValue(value, out translated))
            {
                value = translated;
                return;
            }

            for (int i = 0; i < Patterns.Count; i++)
            {
                if (Patterns[i].Key.IsMatch(value))
                {
                    value = Patterns[i].Key.Replace(value, Patterns[i].Value);
                    return;
                }
            }
        }
    }
}
