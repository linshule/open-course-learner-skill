#!/usr/bin/env python3
"""
fetch_transcript.py — YouTube/Bilibili transcript fetcher for open-course-learner.

Tier 1 subtitle acquisition tool. Attempts multiple methods to fetch
transcripts from YouTube and Bilibili.

Usage:
    python fetch_transcript.py https://youtu.be/VIDEO_ID
    python fetch_transcript.py https://www.youtube.com/watch?v=VIDEO_ID
    python fetch_transcript.py https://www.bilibili.com/video/BV1xx411c7mD
    python fetch_transcript.py <file>  # Read URLs from file, one per line

Output:
    Writes transcript to stdout as markdown with timestamps.
"""

import json
import os
import re
import sys
import tempfile
import subprocess
import urllib.request
import urllib.error
from pathlib import Path

def extract_youtube_id(url):
    """Extract YouTube video ID from various URL formats."""
    patterns = [
        r'(?:youtube\.com/watch\?v=|youtu\.be/|youtube\.com/embed/)([\w-]{11})',
        r'youtube\.com/watch\?.*v=([\w-]{11})',
    ]
    for pattern in patterns:
        m = re.search(pattern, url)
        if m:
            return m.group(1)
    return None

def extract_bilibili_bv(url):
    """Extract Bilibili BV ID from URL."""
    m = re.search(r'bilibili\.com/video/(BV\w+)', url)
    if m:
        return m.group(1)
    return None

def method_yt_dlp(url, lang='en'):
    """Try yt-dlp to download subtitles."""
    try:
        with tempfile.TemporaryDirectory() as tmpdir:
            outtmpl = os.path.join(tmpdir, 'subs')
            cmd = [
                'yt-dlp',
                '--write-auto-subs',
                '--skip-download',
                '--sub-langs', lang,
                '--convert-subs', 'srt',
                '-o', outtmpl,
                url
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
            if result.returncode != 0:
                return None, f"yt-dlp failed: {result.stderr[:200]}"

            # Find the generated .srt or .vtt file
            files = list(Path(tmpdir).glob('*.srt')) + list(Path(tmpdir).glob('*.vtt'))
            if not files:
                return None, "yt-dlp: no subtitle file generated"

            content = files[0].read_text(encoding='utf-8')
            # Parse SRT/VTT to simple text with timestamps
            lines = []
            for line in content.split('\n'):
                line = line.strip()
                # Skip empty lines, sequence numbers, and metadata
                if not line or line.isdigit() or '-->' in line:
                    continue
                # Skip WEBVTT header and formatting
                if line.startswith('WEBVTT') or line.startswith('Kind:') or line.startswith('Language:'):
                    continue
                if re.match(r'^\d{2}:\d{2}', line):
                    continue
                # Remove HTML tags
                line = re.sub(r'<[^>]+>', '', line)
                lines.append(line)

            return '\n'.join(lines), None
    except FileNotFoundError:
        return None, "yt-dlp not installed (try: pip install yt-dlp)"
    except subprocess.TimeoutExpired:
        return None, "yt-dlp timed out"
    except Exception as e:
        return None, f"yt-dlp error: {str(e)}"

def method_youtube_transcript_api(video_id):
    """Try youtube-transcript-api library."""
    try:
        from youtube_transcript_api import YouTubeTranscriptApi
        api = YouTubeTranscriptApi()
        transcript = api.fetch(video_id)
        lines = []
        for item in transcript:
            m, s = divmod(int(item['offset']), 60)
            timestamp = f"[{m:02d}:{s:02d}]"
            text = item['text'].strip()
            lines.append(f"{timestamp} {text}")
        return '\n'.join(lines), None
    except ImportError:
        return None, "youtube-transcript-api not installed (try: pip install youtube-transcript-api)"
    except Exception as e:
        return None, f"youtube-transcript-api error: {str(e)}"

def method_webfetch_youtubetranscript(video_id):
    """Try youtubetranscript.com API."""
    try:
        url = f"https://youtubetranscript.com/?v={video_id}"
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            data = resp.read().decode('utf-8')
            # The site returns HTML with JS-rendered content, not clean JSON
            # Try to find JSON in the HTML
            import html
            text = html.unescape(data)
            # Extract text content between tags
            text = re.sub(r'<[^>]+>', ' ', text)
            text = re.sub(r'\s+', ' ', text).strip()
            if text and len(text) > 100:
                return text, None
            return None, "youtubetranscript.com returned empty/JS-rendered content"
    except Exception as e:
        return None, f"webfetch error: {str(e)}"

def method_bilibili_api(bvid):
    """Fetch Bilibili subtitles via official API."""
    try:
        # Step 1: Get video info (find cid)
        info_url = f"https://api.bilibili.com/x/web-interface/view?bvid={bvid}"
        req = urllib.request.Request(info_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            info = json.loads(resp.read().decode('utf-8'))

        if info.get('code') != 0:
            return None, f"Bilibili API error: {info.get('message', 'unknown')}"
        cid = info['data']['cid']

        # Step 2: Get subtitle URL
        player_url = f"https://api.bilibili.com/x/player/wbi/v2?bvid={bvid}&cid={cid}"
        req = urllib.request.Request(player_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            player = json.loads(resp.read().decode('utf-8'))

        if player.get('code') != 0:
            return None, f"Bilibili player API error: {player.get('message', 'unknown')}"

        subtitles = player.get('data', {}).get('subtitle', {}).get('subtitles', [])
        if not subtitles:
            return None, "No subtitles available (may need login)"

        # Prefer English AI subs, then first available
        target = None
        for sub in subtitles:
            if sub.get('lan') == 'ai-en':
                target = sub
                break
        if not target:
            target = subtitles[0]

        sub_url = target['subtitle_url']
        if sub_url.startswith('//'):
            sub_url = 'https:' + sub_url

        # Step 3: Get subtitle content
        req = urllib.request.Request(sub_url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=15) as resp:
            sub_data = json.loads(resp.read().decode('utf-8'))

        lines = []
        for item in sub_data.get('body', []):
            m, s = divmod(int(item.get('from', 0)), 60)
            timestamp = f"[{m:02d}:{s:02d}]"
            content = item.get('content', '').strip()
            lines.append(f"{timestamp} {content}")

        return '\n'.join(lines), None
    except urllib.error.HTTPError as e:
        return None, f"Bilibili HTTP error: {e.code}"
    except Exception as e:
        return None, f"Bilibili error: {str(e)}"

def fetch_youtube(url):
    """Fetch YouTube transcript using tiered methods."""
    video_id = extract_youtube_id(url)
    if not video_id:
        return None, "Invalid YouTube URL"

    # Tier 1: youtube-transcript-api (pure Python, no external deps issues)
    text, err = method_youtube_transcript_api(video_id)
    if text:
        return text, None

    # Tier 1b: yt-dlp
    text, err2 = method_yt_dlp(url)
    if text:
        return text, None

    # Tier 2: webfetch youtubetranscript.com
    text, err3 = method_webfetch_youtubetranscript(video_id)
    if text:
        return text, None

    return None, f"All methods failed:\n  1. youtube-transcript-api: {err}\n  2. yt-dlp: {err2}\n  3. webfetch: {err3}"

def fetch_bilibili(url):
    """Fetch Bilibili transcript."""
    bvid = extract_bilibili_bv(url)
    if not bvid:
        return None, "Invalid Bilibili URL"
    return method_bilibili_api(bvid)

def format_as_markdown(text, source_url):
    """Format transcript as markdown with metadata."""
    lines = [
        f"# Transcript",
        f"",
        f"Source: {source_url}",
        f"",
        f"---",
        f"",
    ]
    lines.append(text)
    lines.append("")
    lines.append("---")
    return '\n'.join(lines)

def main():
    if len(sys.argv) < 2:
        print("Usage: python fetch_transcript.py <video_url>")
        print("   or: python fetch_transcript.py <urls_file>")
        sys.exit(1)

    url_or_file = sys.argv[1]

    # Check if input is a file with multiple URLs
    if os.path.isfile(url_or_file):
        with open(url_or_file) as f:
            urls = [line.strip() for line in f if line.strip()]
    else:
        urls = [url_or_file]

    for url in urls:
        print(f"\n# Fetching: {url}", file=sys.stderr)

        if 'youtube.com' in url or 'youtu.be' in url:
            text, err = fetch_youtube(url)
        elif 'bilibili.com' in url:
            text, err = fetch_bilibili(url)
        else:
            text, err = None, f"Unsupported platform: {url}"

        if text:
            print(format_as_markdown(text, url))
        else:
            print(f"# ERROR: {err}", file=sys.stderr)

if __name__ == '__main__':
    main()
