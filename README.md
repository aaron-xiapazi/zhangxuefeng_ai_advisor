# 张雪峰志愿顾问 AI 技能

用张雪峰老师的方法，帮你做高考志愿填报和升学规划。

## 这是什么？

这是一个 AI 技能（Skill），把张雪峰老师 **1306个作品、1279场直播、超过100万字** 的内容提炼成了一套结构化的咨询系统。

它不是简单地背张老师的话，而是学会了他的 **方法论**：
- **懂行业** — 知道哪些专业有坑、哪些学校被低估
- **看人下菜碟** — 根据你的分数、家庭、性格给不同建议
- **说人话** — 像靠谱的长辈跟你掏心窝子，不是专家在念PPT

## 怎么用？

### Claude Code / OpenClaw

```bash
# 安装技能
npx skills add https://github.com/aaron-xiapazi/zhangxuefeng_ai_advisor

# 或者手动下载，放到你的 skills 目录
git clone https://github.com/aaron-xiapazi/zhangxuefeng_ai_advisor.git
```

### ChatGPT / 其他 AI 智能体

把 `SKILL.md` 和 `references/` 目录下的内容作为系统提示词（System Prompt）喂给你的 AI 即可。

### OpenAI Agents

项目包含 `agents/openai.yaml` 配置文件，可直接导入 OpenAI Agent。

## 文件结构

```
zhangxuefeng-advisor/
├── SKILL.md                    # 主技能文件（核心提示词）
├── references/
│   ├── case-library.md         # 真实案例库
│   ├── corpus.md               # 语料说明
│   ├── corpus-patterns.md      # 100条语料提炼的高频判断
│   ├── decision-playbook.md    # 决策原则
│   ├── demo-cases.md           # 演示案例
│   ├── judgment-tree.md        # 结构化判断树
│   ├── people-model.md         # 用户画像与隐含信号识别
│   ├── product-blueprint.md    # 产品蓝图
│   ├── regression-set.md       # 回归测试集
│   ├── review-rubric.md        # 质量检查标准
│   ├── search-protocol.md      # 搜索协议
│   └── style-guide.md          # 对话风格指南
├── scripts/
│   ├── build_search_queries.py # 搜索提纲生成
│   ├── find_similar_examples.py# 相似案例查找
│   └── review_regression.py    # 回归测试
├── agents/
│   └── openai.yaml             # OpenAI Agent 配置
└── README.md
```

## 使用效果

输入你的情况（省份、分数、选科、家庭条件、想法），AI 会像张老师一样：

1. **先问清楚** — 不会上来就甩学校列表
2. **先判断** — 一句话说透你的核心矛盾
3. **给策略** — 先说取舍原则，再谈具体方向
4. **提风险** — 明说坑在哪里，不端水

> "闺女，你这个成绩选择面挺宽的。但先别急着看学校，先想明白一个事——你是想以后在大城市扎根呢，还是回来离爸妈近一点？这个想通了，后面就简单了。"

## 持续更新

这个技能会持续迭代：
- 加入更多真实案例
- 优化判断逻辑
- 跟进最新招生政策和数据
- 完善各省份特殊规则

**Star ⭐ 这个项目**，就能收到更新通知。

## 免责声明

本技能仅供参考，不构成正式的志愿填报建议。最终决策请结合官方数据和个人实际情况。涉及录取分数、招生计划等实时数据，AI 会联网查询，但仍建议以各省考试院官方发布为准。

## 致敬

致敬张雪峰老师。他用 1279 场直播、无数次连麦，帮了几百万个家庭。

一个人的精力有限，但他想帮的人没有上限。

这个技能，是想让这份能力继续下去。

---

**作者：** 琦哥聊AI（公众号同名）

**协议：** MIT — 免费使用，自由分享
