# YouTube Transcript Acquisition Guide

## 1. How YouTube Captions Work

YouTube provides captions in three forms:

- **ASR auto-generated**: Machine speech-to-text, available on most videos within minutes. Accuracy varies for technical terms, accents, or background noise.
- **Uploader-provided**: Manually submitted. Most reliable.
- **Community-contributed**: Added by viewers (rare in 2024+). Often disabled by default.

Each track has a language code (`en`, `ja`, `zh-Hans`). Most educational content has English auto-captions.

## 2. Auto-Fetch Workflow

**Step 1 — Extract the video ID.** YouTube URLs follow two patterns:
```
https://www.youtube.com/watch?v=dQw4w9WgXcQ
https://youtu.be/dQw4w9WgXcQ
```
The ID is always `[a-zA-Z0-9_-]{11}`.

**Step 2 — Try the simple API first.** Fetch with `webfetch`:
```
https://youtubetranscript.com/?v={VIDEO_ID}
```
Returns clean JSON:
```json
[
  {"text": "Welcome to this video", "duration": 2.5, "offset": 0},
  {"text": "where we talk about machine learning.", "duration": 3.0, "offset": 2.5}
]
```
This is the preferred method. No page parsing needed.

**Step 3 — Fall back to page HTML.** Fetch the video page:
```
https://www.youtube.com/watch?v={VIDEO_ID}
```
Search for `playerCaptionsTracklistRenderer` in the HTML. Inside it find the `captionTracks` array:
```json
{
  "baseUrl": "https://www.youtube.com/api/timedtext?v=...&lang=en",
  "languageCode": "en",
  "kind": "asr"
}
```
- `kind: "asr"` = auto-generated. No `kind` = uploader-provided.
- `languageCode` is the ISO two-letter code.

**Step 4 — Fetch the caption data.** Take `baseUrl` and fetch it. Append `&fmt=json` for JSON:
```json
{"events": [{"tStartMs": 0, "dDurationMs": 2500, "segs": [{"utf8": "Welcome"}]}]}
```

**Step 5 — Convert to Markdown.** Format as a table with timestamps:
```markdown
| Time | Text |
|------|------|
| 0:00 | Welcome to this video |
| 0:02 | where we talk about machine learning |
```
For long transcripts, plain text with a timestamp every 30 seconds works.

## 3. Manual Fallback

When auto-fetch fails (captions disabled, region block, bot detection):

**Method A — Guide the user:**
1. Open the video in a browser.
2. Click **More** below the description, then **Show transcript**.
3. Copy and paste the text.

**Method B — youtube-dl (if installed):**
```
youtube-dl --write-auto-sub --skip-download --sub-lang en {URL}
```
Strips to a `.vtt` file. Extract text by removing header lines and timestamps.

**Method C — Browser DevTools:**
1. Open the video, open DevTools (F12).
2. Network tab, filter `timedtext`, reload.
3. Click the matching request, copy the response JSON.

## 4. Common Issues

| Problem | Cause | Workaround |
|---------|-------|------------|
| No captionTracks in page data | Captions disabled | Manual fallback |
| Garbled technical terms | ASR accuracy limits | Mention to user; offer manual |
| Page fetch returns consent wall | Region/cookie block | Use youtubetranscript.com |
| HTTP 429 | Rate limited | Add delay; use manual |
| Video unavailable | Removed/private | Inform user |

## 5. Grep Patterns

```
# Extract YouTube video ID from any URL form
(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([\w-]{11})

# Find caption base URL in page HTML
"baseUrl":"([^"]+timedtext[^"]+)"

# Find available language codes in caption tracks
"languageCode":"(\w+)"
```

## 6. Priority Order

1. `youtubetranscript.com/?v={ID}` — simplest, no parsing.
2. Page HTML — parse `ytInitialPlayerResponse` for caption tracks.
3. Manual methods — guide user or use youtube-dl.

## 7. Notes

- YouTube Data API v3 is **not** required. Avoid it unless the user provides a key.
- Do not download video files. Transcript only.
- Mention caption source (ASR vs manual) when presenting results so the user can gauge accuracy.
