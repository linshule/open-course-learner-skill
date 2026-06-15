---
name: "open-course-learner"
description: "Use when the user wants to learn a foreign CS open course with Chinese guidance, including full transcript translation, key-points summary, beginner-friendly explanations, and lab walkthrough documents. Triggers: '帮我学习这门课', '用中文学习[课程名]', '帮我带学[课程名]', 'help me study [course name] in Chinese', 'generate Chinese notes for [course URL]'. Primary platforms: Bilibili and YouTube; other platforms supported via manual fallback."
---

# Open Course Learner (公开课学习助手)

## Overview

This skill lets you help a zero-basis Chinese CS learner study a foreign open course. It takes course URLs (lectures and labs), fetches subtitles from Bilibili or YouTube, translates everything into Chinese with key technical terms preserved, and generates four types of study documents per lecture.

The pipeline has 5 steps: user interaction, content acquisition, content processing, lab walkthrough, and output organization. Each lecture is processed one at a time to stay within context limits.

Target audience: learners who know basic programming (variables, loops, functions) but do NOT know the course subject. They may or may not be comfortable with command-line tools. Always ask about their dev tool proficiency before generating lab materials.

## The Pipeline (5-Step Workflow)

### Step 1: User Interaction

Receive the course information from the user. You need:

- Course name and year (e.g., "MIT 6.824 2020")
- List of lecture URLs (numbered in order)
- List of lab URLs (if any)

**BEFORE proceeding to Step 4 (Lab Walkthrough), you MUST ask:**

"Do you have Go/Python/Java compiler installed? Can you run test commands in your terminal?"

Do NOT assume the user can run code. Based on their answer, decide whether to include runnable test commands or just code with expected output.

Confirm the output directory will be `{course-name-year}/` in the current workspace.

If the user provides only partial information (e.g., just a course name without URLs), ask them to provide the specific lecture and lab URLs.

---

### Step 2: Content Acquisition

For each lecture URL, determine the platform and fetch subtitles.

**Platform auto-detection:**

| URL Pattern | Platform | Action |
|-------------|----------|--------|
| `bilibili.com/video/` | Bilibili | Load `references/bilibili.md`, try auto-fetch via webfetch |
| `youtube.com/watch` or `youtu.be/` | YouTube | Load `references/youtube.md`, try auto-fetch via webfetch |
| Other | Unknown | Load `references/platforms-fallback.md`, guide manual download |

**Auto-fetch flow:**

1. Load the platform-specific reference file.
2. Use `webfetch` to get the video page and extract subtitle/transcript data.
3. If auto-fetch succeeds, parse the subtitle text and proceed.
4. If auto-fetch fails (blocked, no subtitles, wrong format), guide the user to manually download subtitle files (.srt, .ass, .vtt, or plain text) and paste the content.

**Direct text input:** If the user directly pastes subtitle text or transcript content, skip the fetch step and process the provided text directly.

---

### Step 3: Content Processing (per lecture)

For each lecture URL, generate three documents. Load `references/translation-guide.md` for terminology rules and `references/output-templates.md` for file format before starting.

#### a. Full Chinese Transcript

Translate ALL English content to Chinese. Rules:

- Preserve key technical terms in English (Raft, MapReduce, Kubernetes, sharding, consensus, etc.).
- On first occurrence: write `Term(中文解释)`. Example: `Raft(一种分布式共识算法)`.
- On subsequent occurrences: use the English term only.
- Use timestamps or chapter markers if the source has them.
- Never translate code. Translate code comments.
- If any segment is uncertain, mark it with `[注: 此部分翻译可能不准确]`.

#### b. Key Points Summary

Extract the core concepts from the lecture. Remove filler, fluff, and off-topic tangents. Use bullet-point format. Include code snippets where relevant.

Structure:

```
## Key Points

- **Concept 1**: Brief explanation (2-3 sentences)
- **Concept 2**: Brief explanation
- ...

## Code Examples (if applicable)

\`\`\`language
code block
\`\`\`
```

#### c. Beginner-Friendly Explanation

Write in the simplest possible Chinese. Use analogies, metaphors, and real-world parallels.

Approach:

- Assume the reader knows programming basics (what a variable is, what a loop does).
- Assume the reader does NOT know the course subject.
- Start with "Why should I care?" before explaining how it works.
- Use analogies tied to everyday life (e.g., "MapReduce is like ordering food at a restaurant...").
- End with a one-sentence summary anyone can understand.

---

### Step 4: Lab Walkthrough

For each lab URL, generate a step-by-step tutorial document. This is the most involved step.

**Sub-steps:**

1. **Read the lab spec.** Fetch the lab assignment page and test code from the course website.

2. **Research the lab solution.**

   - Write your own implementation based on course materials.
   - Web search for existing discussions or solutions to cross-verify your approach.
   - If test code is obtainable, run the lab test suite to verify correctness.

3. **Write the tutorial document.** Include all of the following:

   - **Complete, working code** that passes all tests. This is NOT pseudo-code. It must be real, compilable/runnable code.
   - **WHY explanation** for every code block: why this approach, why this function, why this parameter value.
   - **Interview prep notes**: what interviewers might ask about this lab, common follow-up questions.
   - **Test verification**: the exact commands to run and the expected output.

4. **Verify correctness.** Either run the tests yourself (if the environment permits) or simulate the expected output based on thorough analysis. Never include code you have not verified.

**Important:** Before starting this step, load `references/translation-guide.md` and `references/output-templates.md`.

---

### Step 5: Output Organization

Write all files into the `{course-name-year}/` directory in the current workspace.

Directory structure (maximum nesting depth: 3 levels):

```
{course-name-year}/
 01-Complete-Transcript/
   L01-{lecture-title}.md
   L02-{lecture-title}.md
   ...
 02-Key-Points/
   L01-{lecture-title}.md
   L02-{lecture-title}.md
   ...
 03-Beginner-Explanation/
   L01-{lecture-title}.md
   L02-{lecture-title}.md
   ...
 04-Lab-Walkthrough/
   Lab01-{lab-name}.md
   Lab02-{lab-name}.md
   ...
```

Naming rules:

- Use only safe filename characters. No colons, quotes, slashes, backslashes, pipes, question marks, or asterisks.
- Replace spaces with hyphens.
- Keep filenames under 80 characters.

Label each file with the following attribution at the bottom:

```
---

*学习辅助材料 - 非官方课程材料*
```

## Platform Support Overview

| Tier | Platforms | Method | Reference File |
|------|-----------|--------|----------------|
| 1 | Bilibili, YouTube | Auto-fetch subtitles via webfetch | `references/bilibili.md`, `references/youtube.md` |
| 2 | Coursera, edX, MIT OCW, others | Guide user to manually download subtitles | `references/platforms-fallback.md` |
| 3 | Any | User pastes text directly | None needed |

Tier 1 is preferred. If auto-fetch fails, fall back to Tier 2. If the user provides text directly, use Tier 3.

## Language Style Guidelines

This is a summary. For full rules, load `references/translation-guide.md`.

**Terminology preservation.** Key CS terms stay in English. First occurrence gets a Chinese gloss in parentheses.

**Code handling.** Never translate code or variable names. Translate comments only.

**Dual style.** Use both styles in the same document:

- **Tongsu (通俗)**: For explaining concepts. Plain language, analogies, everyday examples.
- **Zhuanyehua (专业化)**: For precise definitions. Use exact technical terms.

Example: "MapReduce is like a restaurant kitchen (通俗): many cooks prepare different dishes in parallel... Formally (专业化), MapReduce is a programming model with Map and Reduce phases that process key-value pairs."

**No em dashes.** Use commas, periods, colons, or line breaks instead.

## Quality Rules

1. **Accuracy.** Never fabricate course content, lecture transcripts, or lab solutions. If content is missing, say so.

2. **Verification.** Always test lab code before including it in the output. Run the test suite or simulate expected output. Never include untested code.

3. **Honesty.** Mark uncertain translations with `[注: 此部分翻译可能不准确]`. If you cannot verify a lab solution, state the limitation.

4. **Scope.** Never bypass paywalls, login-required content, or restricted access. If content is behind a login, tell the user they need to provide the content manually.

5. **Self-containment.** Each lecture's markdown file must be self-contained. Do not reference other files. The reader should be able to read one file and understand the full lecture.

6. **Safe filenames.** Use only the following characters in filenames: A-Z, a-z, 0-9, hyphen, underscore, period. No colons, quotes, slashes, backslashes, pipes, question marks, or asterisks.

7. **Attribution.** Every output file must end with: `学习辅助材料 - 非官方课程材料`. Never present the output as official course materials.

8. **Context discipline.** Process ONE lecture per session. Do not batch an entire course in a single session. The output for one lecture includes all 3-4 document types for that single lecture only.

9. **No auto-discovery.** Do not crawl or scrape course websites to discover lectures. The user must provide all URLs explicitly.

10. **No code execution for user code.** Do not execute code provided by the user. Only run test code from the course materials to verify reference implementations.

11. **Lab verification.** Before writing a lab walkthrough, always verify the solution by running the lab test suite or by thorough cross-referencing with existing solutions. Never provide code that has not been verified.

## Reference Files

Read these files on demand when the corresponding situation arises. Do NOT load all of them at the start.

| File | Load When |
|------|-----------|
| `references/bilibili.md` | User provides a Bilibili video URL. Contains subtitle API patterns and fetch steps. |
| `references/youtube.md` | User provides a YouTube video URL. Contains transcript extraction patterns. |
| `references/platforms-fallback.md` | Auto-fetch fails, or user provides a URL from Coursera/edX/MIT OCW/other platforms. |
| `references/translation-guide.md` | Starting Step 3 (Content Processing). Contains terminology rules, CS glossary, and style guidance. |
| `references/output-templates.md` | Generating output files. Contains Markdown templates for all 4 document types. |

## Resources

### references/

Houses the 5 reference documents listed above. Each file focuses on a single concern and is loaded into context only when needed.

### scripts/

No helper scripts are needed for this skill. See `scripts/README.md` for details. All platform fetching is done via webfetch, and lab verification is done interactively.
