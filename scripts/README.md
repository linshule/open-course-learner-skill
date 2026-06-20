# Scripts

Helper scripts for enhanced subtitle acquisition and content processing.

## fetch_transcript.py

Python script for fetching video transcripts from YouTube and Bilibili.

### Prerequisites

```bash
# For YouTube (at least one of):
pip install youtube-transcript-api   # Pure Python, preferred
pip install yt-dlp                   # More robust, supports cookies

# For Bilibili:
# No additional packages needed (uses urllib from stdlib)
```

### Usage

```bash
# Fetch a single video
python fetch_transcript.py https://youtu.be/VIDEO_ID

# Fetch from Bilibili
python fetch_transcript.py https://www.bilibili.com/video/BV1xx411c7mD

# Fetch multiple URLs from a file
python fetch_transcript.py urls.txt
```

### Output

The script outputs markdown-formatted transcript text with timestamps to stdout.

### Fallback Behavior

The script tries multiple methods in order:
1. **youtube-transcript-api** (Python library, direct YouTube API)
2. **yt-dlp** (command-line tool, more robust against blocks)
3. **webfetch fallback** (last resort, uses youtubetranscript.com)

If all methods fail, the script returns an error message with details.
The main agent should then fall back to manual methods (guide the user).
