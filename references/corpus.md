# Corpus

本 skill 可以参考本地整理好的张雪峰作品语料，但不要默认把整库塞进上下文。

## Local corpus

- 作品文件目录：`/Users/tongziqi/code/zhangxuefeng/output`
- 全量清单：`/Users/tongziqi/code/zhangxuefeng/manifest.json`
- 最近 100 条转文案缓存：`/Users/tongziqi/code/zhangxuefeng/cache`

## How to use the corpus

- 想提炼说话风格时，优先读 `references/style-guide.md`。
- 想复核判断逻辑时，优先读 `references/decision-playbook.md`。
- 只有在用户明确要求“更像张雪峰会怎么说”或需要具体话术样本时，再去语料目录里抽样搜索。

推荐搜索方式：

```bash
rg -n "考公|法学|汉语言|计算机|电气|城市|专业优先|学校优先" /Users/tongziqi/code/zhangxuefeng/output
```

## Guardrails

- 语料用于学习判断框架和表达方式，不用于编造“原话”。
- 如果要引用原文，只能短引，并说明是基于本地整理语料。
- 真正给志愿建议时，最新政策和录取数据必须另外联网核实。
