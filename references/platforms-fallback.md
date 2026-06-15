# Fallback Platform Subtitle Guide

Use this guide when auto-acquisition fails or the user provides content from platforms other than Bilibili or YouTube. Walk the user step by step.

---

## Coursera

Coursera courses provide downloadable subtitles for most lectures.

**Steps for the user:**
1. Open the lecture page and play the video.
2. Click **"More"** (three dots menu) below the video player.
3. Select **"Download Subtitle"** or **"Download Transcript"**.
4. A `.srt` or `.txt` file will download. Provide it to the agent.

**If the menu option is missing:**
1. Open browser **DevTools** (`F12`) and go to the **Network** tab.
2. Filter by `srt` or `subtitle`.
3. Play the video. Request entries will appear with subtitle URLs.
4. Copy the URL and open it in a new tab to download the `.srt` file.

**Note:** Most courses require enrollment. Free audit is available for nearly all courses.

---

## edX

edX provides downloadable transcripts in `.txt` and `.srt` formats.

**Steps for the user:**
1. Open the video page.
2. Click the **"Download"** button below the video player.
3. Select **"Download Transcript"**.
4. Choose your format (`.txt` or `.srt`).
5. Provide the downloaded file to the agent.

---

## MIT OpenCourseWare (OCW)

MIT OCW offers full transcripts alongside every lecture video.

**Steps for the user:**
1. Go to the course page on ocw.mit.edu.
2. Select the desired lecture from the syllabus or video list.
3. Look for a **"Transcript"** or **"Captions"** section below the video.
4. Most lectures also have complete **"Lecture Notes"** as PDF.
5. Provide the transcript text or PDF to the agent.

---

## Generic University Course Pages

Many university course sites host subtitles or companion text files.

**Steps for the user:**
1. On the course website, check the **syllabus** page first.
2. Look for links labeled:
   - **"Transcript"**
   - **"Captions"**
   - **"Slides"**
   - **"Lecture Notes"**
3. Formats are usually `.txt`, `.pdf`, or `.srt`.
4. Provide the file or paste the text to the agent.

---

## When User Pastes Text Directly (Tier 3)

If no subtitle file exists and the user provides raw text:

1. Accept any format: plain text, SRT, VTT, ASS.
2. **If SRT / VTT**: timestamps are parsed automatically.
3. **If plain text**: timestamps are not available. Ask the user to:
   - Indicate lecture or chapter boundaries if the text is long.
   - Mark where one slide or topic ends and the next begins (e.g., `---`).

---

## General Fallback Workflow

```
1. Identify the platform from the URL or user statement.
2. Guide the user with platform-specific steps to get the subtitle file.
3. User provides the subtitle text (paste, file upload, or URL).
4. Process as normal: translate, summarize, extract key points, etc.
```

---

## Reminders

- Do not bypass login walls, paywalls, or violate any platform's terms of service.
- Free audit or publicly available content only.
