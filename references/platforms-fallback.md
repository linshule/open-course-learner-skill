# Fallback Platform Subtitle Guide

Use this guide when:
1. Auto-acquisition fails (blocked, timeout, no subtitles)
2. User provides content from platforms other than Bilibili/YouTube
3. User provides lecture notes URLs instead of video URLs

## Lecture Notes as Primary Content Source

Many courses provide detailed lecture notes (`.txt`, `.pdf`, `.md`). These are often **more accurate and structured** than video subtitles. When available, use them as the primary content source.

### How to detect lecture notes

When a user provides a course URL (not a video URL):

1. Fetch the course homepage / schedule page.
2. Look for links labeled: "Notes", "Lecture Notes", "Slides", "Readings".
3. Common URL patterns:
   - `.../notes/l01.txt`
   - `.../notes/l01.pdf`
   - `.../slides/lec1.pdf`
4. If found: **fetch these notes** as the primary content source.
5. If not found: fall back to video subtitle acquisition.

### Combining lecture notes with video

If both lecture notes and video URL are available:
1. Use lecture notes as the primary content structure (they have correct ordering and terminology).
2. Use video subtitles for supplementary material (verbal explanations, examples, Q&A).

---

Starting guide content below for video subtitles:

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
