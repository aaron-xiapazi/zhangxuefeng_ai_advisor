#!/usr/bin/env python3
import argparse
import re


def detect_intents(query: str) -> list[str]:
    intents = []
    if re.search(r"选科|科目|历史|物理|化学|政史地|史地政", query):
        intents.append("subject_requirements")
    if re.search(r"学校|大学|院校|招生", query):
        intents.append("school_recruitment")
    if re.search(r"专业|法学|汉语言|财会|会计|电气|计算机|师范|医学", query):
        intents.append("major_details")
    if re.search(r"分数|位次|排名|能不能上|录取", query):
        intents.append("score_rank")
    if re.search(r"强基|专项|提前批|公费生|定向", query):
        intents.append("special_rules")
    return intents


def infer_sources(intents: list[str]) -> list[str]:
    sources = [
        "省教育考试院 / 招生考试院",
        "阳光高考 / 学校本科招生网",
        "学校当年招生章程 / 专业选科要求",
    ]
    if "score_rank" in intents:
        sources.append("最近年份录取位次 / 专业组信息")
    return sources


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("query")
    args = parser.parse_args()

    q = args.query.strip()
    intents = detect_intents(q)
    print("建议搜索顺序：")
    for idx, source in enumerate(infer_sources(intents), start=1):
        print(f"{idx}\t{source}")

    print("\n建议查询主题：")
    for intent in intents:
        print(f"- {intent}")

    print("\n建议搜索问句：")
    if "subject_requirements" in intents:
        print(f'- "{q} 选科要求 官方"')
        print(f'- "{q} 招生章程 选考科目要求 官方"')
    if "school_recruitment" in intents:
        print(f'- "{q} 本科招生网 官方"')
        print(f'- "{q} 招生章程 官方"')
    if "major_details" in intents:
        print(f'- "{q} 专业目录 就业方向 官方"')
        print(f'- "{q} 专业介绍 培养方案 官方"')
    if "score_rank" in intents:
        print(f'- "{q} 录取位次 官方"')
        print(f'- "{q} 专业组 位次 官方"')
    if "special_rules" in intents:
        print(f'- "{q} 招生章程 官方"')
    if not intents:
        print(f'- "{q} 官方"')

    print("\n回答落点：")
    print("- 回答里带年份")
    print("- 先说查到的事实")
    print("- 再说这个事实对建议的影响")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
