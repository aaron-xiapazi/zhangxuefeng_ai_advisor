#!/usr/bin/env python3
import argparse
import json
import re
from pathlib import Path


MANIFEST = Path("/Users/tongziqi/code/zhangxuefeng/manifest.json")


KEYWORDS = [
    "财会", "会计", "审计", "汉语言", "法学", "师范", "考公", "考编",
    "就业", "考研", "女生", "文科", "理工科", "城市", "位次", "普通家庭",
    "稳定", "医学", "选科", "电气", "计算机", "国网", "东北", "辽宁",
    "历史", "高二", "高三", "专业", "学校", "规划", "院校", "录取", "省",
    "体面", "离家近", "大城市", "没方向", "老师", "孩子"
]

CASE_PRIORS = {
    "汉语言和财会选哪一个呢 #张雪峰老师 #升学规划 #院校规划+2025-04-21.txt": {
        "普通家庭": 6, "文科": 6, "女生": 5, "稳定": 6, "财会": 9, "汉语言": 9, "师范": 6
    },
    "中低分数段女生有哪些选择？ #张雪峰老师 #升学规划 #院校规划+2026-03-06.txt": {
        "女生": 8, "稳定": 5, "普通家庭": 4, "就业": 4
    },
    "评论区留言：法学本科好就业吗？ #张雪峰老师 #升学规划#评论区留言+2026-03-23.txt": {
        "法学": 9, "就业": 6, "考公": 5, "考研": 6, "体面": 4
    },
    "分数考高考低对专业选择的影响 #张雪峰老师 #升学规划 #院校规划+2026-02-27.txt": {
        "文科": 5, "理工科": 5, "城市": 6, "专业": 4
    },
    "你的专业上学地点和就业地点关系有多大 #张雪峰老师 #升学规划 #院校规划+2025-04-04.txt": {
        "城市": 8, "就业": 5, "文科": 4
    },
    "选科怎么选给你说得明明白白 #张雪峰老师 #升学规划 #院校规划+2026-01-05.txt": {
        "选科": 10, "历史": 5, "理工科": 5, "高二": 3, "高三": 3
    },
    "中低分数段该如何规划 #张雪峰老师 #升学规划 #院校规划+2025-04-25.txt": {
        "稳定": 6, "普通家庭": 4, "就业": 5, "规划": 9
    },
    "哪些专业适合考公，考公的前提是什么 #张雪峰老师 #升学规划 #院校规划+2025-04-11.txt": {
        "考公": 10, "专业": 6
    },
    "评论区留言：金属材料工程需要考研吗？ #张雪峰老师 #评论区留言+2026-03-24.txt": {
        "考研": 10, "专业": 5
    },
    "如何找到你心仪的学校，记住这几步方法 #张雪峰老师 #升学规划 #院校规划+2025-03-19.txt": {
        "学校": 8, "专业": 6, "位次": 7, "录取": 6, "省": 4
    },
    "报志愿要有一级学科思维 #张雪峰老师 #升学规划 #院校规划+2026-01-30.txt": {
        "专业": 6, "学校": 4
    },
    "如何用本科专业目录报志愿避坑 #张雪峰老师 #升学规划 #院校规划+2026-01-23.txt": {
        "专业": 7, "学校": 3
    },
}


def normalize(text: str) -> str:
    return re.sub(r"\s+", "", text)


def extract_hints(query: str) -> dict:
    hints = {kw: 0 for kw in KEYWORDS}
    for kw in KEYWORDS:
        if kw in query:
            hints[kw] += 1
    if any(word in query for word in ["普通家庭", "家里没资源", "没有资源"]):
        hints["普通家庭"] += 2
    if any(word in query for word in ["文科", "历史", "史地政", "史政地"]):
        hints["文科"] += 2
    if any(word in query for word in ["女生", "女孩", "妹妹", "女儿"]):
        hints["女生"] += 2
        hints["孩子"] += 1
    if any(word in query for word in ["稳", "稳定", "稳一点"]):
        hints["稳定"] += 2
    if any(word in query for word in ["体面", "听起来好", "名头"]):
        hints["体面"] += 2
    if any(word in query for word in ["说不太清", "说不清", "讲不清"]):
        hints["没方向"] += 2
    if any(word in query for word in ["东北", "辽宁"]):
        hints["城市"] += 1
    if any(word in query for word in ["没方向", "没有方向", "没什么特别明确", "没想法"]):
        hints["专业"] += 1
        hints["没方向"] += 2
    if any(word in query for word in ["规划", "怎么规划"]):
        hints["规划"] += 2
    if any(word in query for word in ["学校", "院校", "大学"]):
        hints["学校"] += 2
        hints["院校"] += 1
    if any(word in query for word in ["录取", "能不能报", "可报"]):
        hints["录取"] += 2
    if any(word in query for word in ["某省", "在辽宁", "在河北", "在山东", "在江苏", "在浙江"]):
        hints["省"] += 2
    if any(word in query for word in ["离家近", "离家", "本地", "回家"]):
        hints["离家近"] += 2
        hints["城市"] += 1
    if any(word in query for word in ["大城市", "省会", "江浙沪"]):
        hints["大城市"] += 2
        hints["城市"] += 2
    if any(word in query for word in ["不太乐意", "不想回", "不想留在省内"]):
        hints["城市"] += 2
        hints["大城市"] += 1
    if any(word in query for word in ["不想一直考试", "不想老考试"]):
        hints["考公"] += 1
        hints["就业"] += 1
    if any(word in query for word in ["孩子", "家长", "老师"]):
        hints["孩子"] += 1
        hints["老师"] += 1
    score_hint = re.search(r"([45]\d{2})分", query)
    if score_hint:
        score = int(score_hint.group(1))
        if 430 <= score <= 560:
            hints["稳定"] += 1
            hints["普通家庭"] += 1
    return hints


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query", help="User query")
    parser.add_argument("--top", type=int, default=8)
    args = parser.parse_args()

    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    query = normalize(args.query)
    hints = extract_hints(query)
    matched_keywords = [kw for kw, v in hints.items() if v > 0]

    scored = []
    for item in manifest["items"]:
        if not item.get("analyzed"):
            continue
        path = Path(item["file_path"])
        if not path.exists():
            continue
        text = normalize(path.read_text(encoding="utf-8"))
        score = 0
        for kw in matched_keywords:
            if kw in text:
                score += 2 + hints[kw]
        if any(word in query for word in ["妹妹", "女儿", "女孩"]) and any(word in text for word in ["女孩", "女生", "女孩子"]):
            score += 4
        if any(word in query for word in ["没方向", "没什么特别明确", "没有明确"]) and any(word in text for word in ["怎么选", "方向", "优先", "排序"]):
            score += 3
        if any(word in query for word in ["能不能报", "录取", "某学校某专业"]) and any(word in text for word in ["位次", "学校", "专业", "够哪些专业"]):
            score += 4
        if any(word in query for word in ["体面", "听起来好"]) and any(word in text for word in ["体面", "好就业", "别把它想得太美"]):
            score += 4
        if any(word in query for word in ["说不太清", "说不清"]) and any(word in text for word in ["真喜欢", "觉得喜欢", "喜欢", "代价"]):
            score += 4
        if any(word in query for word in ["离家近", "大城市", "省会", "不想回老家"]) and any(word in text for word in ["城市", "地点", "就业地点", "地域"]):
            score += 4
        if any(word in query for word in ["不想一直考试", "不想老考试"]) and any(word in text for word in ["考公", "岗位", "专业要求"]):
            score += 3
        if any(word in query for word in ["孩子没想法", "没什么特别明确", "没想法"]) and any(word in text for word in ["怎么选", "方向", "优先", "排序", "女生有哪些选择"]):
            score += 4
        priors = CASE_PRIORS.get(item["file_name"], {})
        for kw, weight in priors.items():
            if hints.get(kw, 0) > 0:
                score += weight
        if score > 0:
            scored.append((score, item["file_name"], str(path)))

    scored.sort(key=lambda x: (-x[0], x[1]))
    for score, name, path in scored[: args.top]:
        print(f"{score}\t{name}\t{path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
