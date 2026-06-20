# YouTube Transcript Acquisition Guide

## 1. How YouTube Captions Work

YouTube provides captions in three forms:

- **ASR auto-generated**: Machine speech-to-text, available on most videos within minutes. Accuracy varies for technical terms, accents, or background noise.
- **Uploader-provided**: Manually submitted. Most reliable.
- **Community-contributed**: Added by viewers (rare in 2024+). Often disabled by default.

Each track has a language code (`en`, `ja`, `zh-Hans`). Most educational content has English auto-captions.

## 2. Auto-Fetch Workflow (Priority Order)

The skill tries the following methods **in order**, moving to the next if the current one fails.

### Tier 1 — yt-dlp (Python, preferred)

Use the `youtube-transcript-api` Python library or `yt-dlp` for direct subtitle extraction:

**Method A — youtube-transcript-api (recommended):**
```bash
pip install youtube-transcript-api
python -c "
from youtube_transcript_api import YouTubeTranscriptApi
import json
api = YouTubeTranscriptApi()
transcript = api.fetch('{VIDEO_ID}')
with open('transcript.json', 'w') as f:
    json.dump(transcript, f, ensure_ascii=False)
# Output format: [{'text': '...', 'duration': 2.5, 'offset': 0}, ...]
"
```

**Method B — yt-dlp:**
```bash
pip install yt-dlp
yt-dlp --write-auto-subs --skip-download --sub-langs en --convert-subs srt -o "transcript" "{URL}"
```
If blocked by YouTube's bot detection, try:
```bash
yt-dlp --cookies-from-browser chrome --write-auto-subs --skip-download --sub-langs en "{URL}"
```

### Tier 2 — webfetch to youtubetranscript.com

Fetch with `webfetch`:
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

### Tier 3 — webfetch YouTube page HTML

Fetch the video page:
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

Fetch the caption data from `baseUrl`. Append `&fmt=json` for JSON:
```json
{"events": [{"tStartMs": 0, "dDurationMs": 2500, "segs": [{"utf8": "Welcome"}]}]}
```

## 3. Format Transcript

Convert to Markdown. Format as a table with timestamps:
```markdown
| Time | Text |
|------|------|
| 0:00 | Welcome to this video |
| 0:02 | where we talk about machine learning |
```
For long transcripts, plain text with a timestamp every 30 seconds works.

Always note the caption source (ASR auto-generated vs uploader-provided) so the user can gauge accuracy.

## 4. Manual Fallback (when all auto methods fail)

**Method A — Guide the user:**
1. Open the video in a browser.
2. Click **More** below the description, then **Show transcript**.
3. Copy and paste the text.

**Method B — Browser DevTools:**
1. Open the video, open DevTools (F12).
2. Network tab, filter `timedtext`, reload.
3. Click the matching request, copy the response JSON.

## 5. Common Issues

| Problem | Cause | Workaround |
|---------|-------|------------|
| yt-dlp: "Sign in to confirm you're not a bot" | YouTube IP block | Use `--cookies-from-browser` or fall back to manual |
| youtube-transcript-api: RequestBlocked | Cloud IP blocked | Use yt-dlp with cookies, or manual fallback |
| No captionTracks in page data | Captions disabled | Manual fallback |
| Garbled technical terms | ASR accuracy limits | Mention to user; offer manual |
| Page fetch returns consent wall | Region/cookie block | Use yt-dlp or manual fallback |
| HTTP 429 | Rate limited | Add delay; use manual |

## 6. Grep Patterns

```
# Extract YouTube video ID from any URL form
(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([\w-]{11})

# Find caption base URL in page HTML
"baseUrl":"([^"]+timedtext[^"]+)"

# Find available language codes in caption tracks
"languageCode":"(\w+)"
```

## 7. Priority Order Summary

1. **yt-dlp / youtube-transcript-api** — most reliable against IP blocks
2. **youtubetranscript.com webfetch** — simple, no parsing
3. **YouTube page HTML** — parse `ytInitialPlayerResponse`
4. **Manual methods** — guide user or use DevTools

## 8. Notes

- YouTube Data API v3 is **not** required. Avoid it unless the user provides a key.
- Do not download video files. Transcript only.
- Mention caption source (ASR vs manual) when presenting results so the user can gauge accuracy.
- If Python libraries are not available in the environment, skip directly to Tier 2 (webfetch).
