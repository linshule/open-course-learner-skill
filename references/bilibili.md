# Bilibili Subtitle Acquisition Guide

Reference for fetching subtitles from Bilibili video URLs. Load when user provides a `bilibili.com/video/` URL.

## How Bilibili Subtitles Work

Bilibili offers AI-generated subtitles (字幕) for most videos. Subtitles are served through a 3-step API chain:

```
Step 1: GET /x/web-interface/view  → get video metadata + cid
Step 2: GET /x/player/wbi/v2       → get subtitle_url from player data
Step 3: GET {subtitle_url}         → get actual subtitle JSON
```

Subtitle JSON format: `body` array of segments with `content` (text), `from` (start time in seconds), `to` (end time in seconds).

## Auto-Fetch Workflow

### 1. Extract BV ID

```
URL pattern: https://www.bilibili.com/video/BV1xx411c7mD
Grep:        bilibili\.com/video/(BV\w+)
```

Multi-P videos use `?p=N`. Each part has a different cid.

### 2. Get Video Info (find cid)

```
GET https://api.bilibili.com/x/web-interface/view?bvid={BVID}
```

Response fields:

```json
{"code":0,"data":{"cid":123456789,"pages":[{"cid":123456789,"part":"Part 1"},{"cid":987654321,"part":"Part 2"}]}}
```

If URL has `?p=2`, use `data.pages[1].cid`. Otherwise use `data.cid`.

### 3. Get Subtitle URL

```
GET https://api.bilibili.com/x/player/wbi/v2?bvid={BVID}&cid={CID}
```

Use `wbi/v2` endpoint (not older `player/v2`, which may return empty data).

```json
{"code":0,"data":{"subtitle":{"subtitles":[
  {"lan":"ai-zh","lan_doc":"中文（自动生成）","subtitle_url":"//aisubtitle.hdslb.com/bfs/ai_subtitle/prod/..."},
  {"lan":"ai-en","lan_doc":"英语（自动生成）","subtitle_url":"//aisubtitle.hdslb.com/bfs/ai_subtitle/prod/..."}
],"need_login_subtitle":false}}}
```

**Key notes:**
- For foreign CS courses, prefer `ai-en` (English AI subs), then `ai-zh`.
- `subtitle_url` is protocol-relative (starts with `//`). Always prepend `https:`.
- Empty `subtitles` or `need_login_subtitle: true` means login required. Fall back to manual.

### 4. Fetch Subtitle JSON

```
GET https:{subtitle_url}
```

No additional headers needed. The URL carries an `auth_key`.

### 5. Parse into Plain Text

```json
{"body":[
  {"from":0.0,"to":4.5,"content":"Welcome to today's lecture."},
  {"from":4.5,"to":9.2,"content":"We will cover the Raft algorithm."}
]}
```

Extract `body` array, format each as: `[MM:SS] content`. Timestamp: `[MM:SS]` where MM = floor(from/60), SS = floor(from%60).

```
[00:00] Welcome to today's lecture.
[00:04] We will cover the Raft algorithm.
```

### Quick Workflow Summary

```
1. bvid = extract_bvid(url)
2. info = webfetch "https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
3. cid  = info.data.pages[page_index].cid ?? info.data.cid
4. player = webfetch "https://api.bilibili.com/x/player/wbi/v2?bvid={bvid}&cid={cid}"
5. subs = player.data.subtitle.subtitles
6. target = subs.find(lan=="ai-en") ?? subs[0]
7. sub_data = webfetch "https:" + target.subtitle_url
8. lines = sub_data.body.map(s => format_time(s.from) + " " + s.content)
9. return lines.join("\n")
```

## Manual Fallback

**DevTools method (recommended):**
1. Open video page in Chrome/Firefox/Edge, press F12.
2. Go to Network tab, filter by "wbi/v2" or "subtitle".
3. Refresh page, find the `player/wbi/v2` request.
4. Copy `subtitle_url` from response JSON.
5. Open that URL in a new tab to download subtitle JSON.
6. Send the JSON content to the agent.

**Browser extension:** Use "Bilibili CC Subtitle" to download .srt/.json file, then paste content.

**Direct text:** If user provides transcript text directly, skip fetch and process it.

## Common Issues

| Issue | Cause | Fix |
|-------|-------|-----|
| Empty `subtitles` | Not logged in, or no subs exist | Guide DevTools manual download |
| `need_login_subtitle: true` | Login required | Same as above |
| 403/412 response | Anti-scraping rate limit | Back off, fall back to manual |
| Garbage subtitle text | Old `player/v2` returning fake data | Use `wbi/v2` endpoint |
| No subtitles at all | Old video or burned-in subs | Mark unavailable; ask user for transcript |
| Wrong multi-P timing | Wrong cid for the part | Check `?p=N`, use `pages[N-1].cid` |

## Important Constraints

1. **Do NOT bypass login/membership restrictions.** If subtitles require login, inform the user.
2. **Do NOT download video files.** This guide is for subtitle text only.
3. **AI subtitles may have errors.** Technical terms and proper names are frequently mis-transcribed.
4. **Rate limits apply.** On 412 responses, fall back to manual mode.
5. **Region-restricted content.** If API errors suggest geo-blocking, inform the user and use manual fallback.

## Grep Patterns for Quick Reference

```
# Extract BVID from URL
bilibili\.com/video/(BV\w+)

# Find cid in view API response
"cid":(\d+)

# Find subtitle URLs in player API response
"subtitle_url":"([^"]+)"

# Language tags in subtitle list
"lan":"([^"]+)"
```
