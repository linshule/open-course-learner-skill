<div align="center">

# 公开课学习助手 (open-course-learner)

<p align="center">
  <sub>by <a href="https://github.com/linshule">@linshule</a></sub>
</p>

> *「把最好的 CS 公开课，变成你最趁手的中文学习笔记」*

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![OpenCode Skill](https://img.shields.io/badge/OpenCode-Skill-blue)](#)
[![skills.sh](https://img.shields.io/badge/skills.sh-Compatiable-brightgreen)](https://skills.sh)

<br>

**零基础中文学习者，也能系统地啃下国外 CS 公开课。**

<br>

输入课程 URL（Bilibili / YouTube），自动完成：
完整中文文字记录 · 重点知识概括 · 零基础通俗讲解 · Lab 带做文档

[效果示例](#-效果示例) · [安装](#-安装) · [核心能力](#-核心能力) · [参考资料](#-参考资料) · [仓库结构](#-仓库结构)

</div>

---

## 🎯 效果示例

### 输入

```
帮我用中文学习 MIT 6.824 2020 的第一节课
视频链接：https://www.youtube.com/watch?v=cQP8WApzIQQ
```

### 输出

Skill 自动生成的目录结构：

```
MIT-6.824-2020/
├── 01-完整文字记录/
│   └── L01-Introduction-to-Distributed-Systems.md
├── 02-重点概括/
│   └── L01-Introduction-to-Distributed-Systems.md
└── 03-通俗理解/
    └── L01-Introduction-to-Distributed-Systems.md
```

### 每个文件的内容示例

<details>
<summary>📝 01-完整文字记录 — 展开查看片段</summary>

```markdown
# L01: Introduction to Distributed Systems — 完整中文文字记录

MIT 6.824 2020 | Lecture 1

---

[00:00] **Robert Morris**: 大家好，欢迎来到 6.824。
This is a course about **distributed systems(分布式系统)** —
a collection of computers that work together to appear as a single computer.

[02:15] 为什么需要分布式系统？
因为单台机器的性能有物理极限。
More CPUs, more memory, more disk — 终究会遇到瓶颈。
而分布式系统可以让你用很多台普通机器，
达到一台超级计算机的能力。

[05:30] 这门课的核心主题：
- **Fault Tolerance(容错)** — 部分机器挂了，系统还能工作
- **Replication(复制)** — 多副本保证数据不丢
- **Consistency(一致性)** — 多副本之间的数据要一致
- **MapReduce(一种分布式编程模型)** — 这是本课的第一个 lab

---

*学习辅助材料 - 非官方课程材料*
```

</details>

<details>
<summary>📌 02-重点概括 — 展开查看片段</summary>

```markdown
# L01: Introduction to Distributed Systems — 重点概括

## 核心概念

- **分布式系统的定义**: 多台计算机协作，对外表现为单一系统
- **为什么需要分布式**: 单机性能有物理极限（CPU、内存、磁盘）
- **主要挑战**: 并发、网络延迟、部分故障、数据一致性
- **MapReduce**: 一个编程模型，把大任务拆成 Map(映射) 和 Reduce(归约) 两个阶段

## 关键术语

| 术语 | 通俗理解 |
|------|----------|
| Fault Tolerance | 挂了几个机器，系统照常跑 |
| Replication | 多存几份副本，不怕丢 |
| Consistency | 所有副本看到的数据一样 |
| RPC | 让一台机器调用另一台机器的函数 |
```
</details>

<details>
<summary>🧠 03-通俗理解 — 展开查看片段</summary>

```markdown
# L01: Introduction to Distributed Systems — 通俗理解

## 为什么要学这个？

想象一下你开了一家餐厅。一开始你一个人就能搞定所有事——
做菜、收银、招呼客人。后来客人多了，你忙不过来，
于是你请了厨师、收银员、服务员——这就叫分布式系统。

**通俗版本**: 分布式系统 = 一群人一起干活，看起来像一个人。
每个人负责一部分，互相配合。

**专业化版本**: 分布式系统 = 通过网络连接的多台自治计算机，
它们通过消息传递协作，对外表现为单一一致的计算系统。

## 一句话总结

分布式系统就是「人多力量大」——用很多台普通电脑，
做成一台超级电脑才能做的事。
```
</details>

<details>
<summary>💻 04-Lab带做 — 示例</summary>

```markdown
# Lab 1: MapReduce — 带做教程

## 实验目标
实现一个简化版的 MapReduce 框架，
让你的程序可以自动将任务分发给多个 worker 并行处理。

## 前置条件
需要安装 Go 1.13+ 并配置好 GOPATH。

## 第一步：理解框架结构

// mrcoordinator.go 是协调者，负责任务分发
// mrworker.go 是工作者，负责实际计算
// mrapps/ 目录下是 map 和 reduce 函数的具体实现

## 第二步：实现任务分发
[完整代码 + WHY 解释]

## 验证
cd src/main && go test -run TestBasic
# 预期输出: PASS
```
</details>

---

## 📦 安装

### 方式一：一行命令（推荐）

```bash
npx skills add linshule/open-course-learner-skill
```

### 方式二：手动安装

```bash
git clone https://github.com/linshule/open-course-learner-skill.git ~/.agents/skills/open-course-learner
```

### 方式三：直接引用 SKILL.md

即使你的 runtime 不支持自动加载 Skills，也可以把 `SKILL.md` 的内容粘贴进对话使用。

### 使用

装好后，直接告诉你的 agent：

```
请帮我用中文学习 [课程名]，课程链接：[URL]
帮我带学 [课程名]，视频和 Lab 链接如下：...
用中文总结这节课：[URL]
```

---

## 🧭 核心能力

### 5 步处理流水线

| 步骤 | 做什么 | 参考文件 |
|------|--------|----------|
| **1. 用户交互** | 收集课程信息，询问开发工具水平 | — |
| **2. 内容获取** | 从 Bilibili/YouTube 自动获取字幕，失败则引导手动下载 | `references/bilibili.md`, `references/youtube.md` |
| **3. 内容处理** | 翻译 → 转录 → 摘要 → 通俗讲解 | `references/translation-guide.md` |
| **4. Lab 带做** | 编写完整代码 + WHY 解释 + 验证正确性 | — |
| **5. 输出组织** | 按 `{课程名-年份}/` 目录结构写入文件 | `references/output-templates.md` |

### 支持平台

| 等级 | 平台 | 方式 |
|------|------|------|
| 🟢 自动 | Bilibili, YouTube | webfetch 自动获取字幕 |
| 🟡 手动 | Coursera, edX, MIT OCW 等 | 引导用户手动下载字幕文件 |
| 🔵 直贴 | 任意平台 | 用户直接粘贴文字内容 |

### 质量保障

- **术语保留**: 关键 CS 术语保留英文，首次出现标注中文解释
- **代码验证**: Lab 代码经过测试 + 联网搜索双重验证
- **双重风格**: 通俗类比 + 专业化定义并存
- **安全边界**: 不绕过付费墙、不自动爬取、不替用户执行代码

---

## 📚 参考资料

Skill 内置了 5 份参考文档，按需加载：

| 文件 | 用途 | 内容概要 |
|------|------|----------|
| `references/bilibili.md` | Bilibili 字幕获取 | API 调用链、cid 提取、手动降级方案、常见错误处理 |
| `references/youtube.md` | YouTube 转录获取 | 3 种获取方式优先级、ASR 字幕处理、多语言处理 |
| `references/platforms-fallback.md` | 其他平台降级 | Coursera/edX/MIT OCW 字幕获取指南 |
| `references/translation-guide.md` | 技术翻译指南 | 6 条翻译规则 + 68 个 CS 术语中英文对照表 |
| `references/output-templates.md` | 输出格式模板 | 4 种文档类型的 Markdown 模板 |

---

## 📂 仓库结构

```
open-course-learner-skill/
├── README.md                       # 本文件
├── SKILL.md                        # 核心工作流（可直接安装使用）
├── agents/
│   └── openai.yaml                 # UI 元数据
├── references/
│   ├── bilibili.md                 # Bilibili 字幕获取指南
│   ├── youtube.md                  # YouTube 转录获取指南
│   ├── platforms-fallback.md       # 其他平台降级方案
│   ├── translation-guide.md        # CS 技术翻译指南 + 68 个术语表
│   └── output-templates.md         # 4 种输出模板
└── scripts/
    └── README.md                   # 说明（无辅助脚本）
```

---

## 📄 许可证

MIT — 随便用，随便改。

---

<div align="center">

*学 CS 公开课，不再被语言和基础卡住。*

<br>

Made by [@linshule](https://github.com/linshule)

</div>
