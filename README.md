# 🎓 公开课学习助手 (open-course-learner)

[![OpenCode Skill](https://img.shields.io/badge/OpenCode-Skill-blue)](#)

---

## 📖 介绍 | Introduction

**中文** | [English ↓](#introduction-en)

**公开课学习助手** 是一个 [OpenCode](https://github.com/opencode-ai/opencode) Skill，专门帮助**零基础中文学习者**系统性地学习国外计算机科学公开课。

你只需提供课程链接，它会自动完成：
- 📝 完整中文文字记录（保留关键英文术语）
- 📌 重点知识概括
- 🧠 零基础通俗讲解
- 💻 Lab 带做文档（完整代码 + WHY 解释 + 面试要点）

优先支持 **Bilibili** 和 **YouTube** 平台，其他平台提供人工降级方案。

---

<a id="introduction-en"></a>
**English**

**Open Course Learner** is an [OpenCode](https://github.com/opencode-ai/opencode) Skill designed for **zero-basis Chinese learners** to systematically study foreign Computer Science open courses.

Provide course URLs, and it will automatically generate:
- 📝 Full Chinese transcript (with key English terms preserved)
- 📌 Key points summary
- 🧠 Beginner-friendly explanations in plain Chinese
- 💻 Lab walkthrough docs (complete code + WHY explanations + interview prep)

**Bilibili** and **YouTube** are fully supported with auto-fetching. Other platforms are supported via manual fallback.

---

## 🚀 快速开始 | Quick Start

### 中文

安装此 Skill 后，在 OpenCode 中直接说：

```
请帮我用中文学习 MIT 6.824 2020，这是视频链接：
https://www.youtube.com/watch?v=xxx
```

或者批量处理整门课：

```
帮我带学 GAMES101，视频链接在下面：
https://www.bilibili.com/video/BVxxx  (Lecture 1)
https://www.bilibili.com/video/BVxxx  (Lecture 2)
...
Lab 链接：
https://games-cn.org/intro-graphics/lab-1/
```

### English

After installing this Skill, just say in OpenCode:

```
Help me study MIT 6.824 2020 in Chinese, video link:
https://www.youtube.com/watch?v=xxx
```

---

## 📂 输出结构 | Output Structure

```
{课程名-年份}/
├── 01-完全文字记录/          # Complete Transcript (CN)
├── 02-重点概括/              # Key Points Summary (CN)
├── 03-通俗理解/              # Beginner Explanation (CN)
└── 04-Lab带做/              # Lab Walkthrough (CN)
```

所有文件均为 Markdown 格式，中文为主，关键英文术语保留并标注。每一讲生成独立文件，方便按进度学习。

---

## ✅ 核心原则 | Core Principles

| 原则 | 说明 |
|------|------|
| **术语保留** | 关键 CS 术语保留英文，首次出现标注中文解释 |
| **双重风格** | 通俗类比 + 专业化定义并存 |
| **代码可运行** | Lab 代码经过测试验证，不是伪代码 |
| **WHY 优先** | 解释每段代码为什么这么写 |
| **安全边界** | 不绕过付费墙、不自动爬取、不替用户执行代码 |

---

## 🛠️ 技术细节 | Technical Details

- **技能位置**: `~/.agents/skills/open-course-learner/`
- **内容获取**: 通过 `webfetch` 工具从 Bilibili/YouTube 获取字幕
- **翻译引擎**: 由大模型驱动，配合内置 CS 术语表（68 个核心术语）
- **Lab 验证**: 模型通过测试程序 + 联网搜索双重验证代码正确性
- **验证通过**: `quick_validate.py` 校验通过 ✅

---

## 📄 许可 | License

MIT
