# Bark Audio Narration Setup Guide

This guide walks you through adding audio narration to Bolt's AI Adventure using Bark (open source, free forever).

---

## Overview

- **Service:** Bark (by Suno AI)
- **Voice:** Australian female (v2/en_speaker_5)
- **Cost:** Free forever (open source)
- **Setup time:** ~40 minutes (first run downloads models)
- **Output:** 9 MP3 files in `/audio` folder
- **Credit card needed:** No

---

## Step 1: Install Python Libraries (5 min)

```bash
pip install git+https://github.com/suno-ai/bark.git scipy
```

---

## Step 2: Install FFmpeg for MP3 Conversion (2 min)

```bash
brew install ffmpeg
```

---

## Step 3: Run the Generation Script (5-10 min)

```bash
python generate_audio_bark.py
```

**First run will be slow** — it downloads ~5GB of models. Subsequent runs are fast.

---

## Step 4: Convert WAV to MP3 (2 min)

```bash
cd audio
for f in *.wav; do ffmpeg -i "$f" "${f%.wav}.mp3"; done
cd ..
rm audio/*.wav
```

---

## Step 5: Add Audio to HTML

Add "Read to me" buttons and audio elements to `index.html`.

---

## Voice Options

| Preset | Accent | Gender |
|--------|--------|--------|
| `v2/en_speaker_0` | American | Male |
| `v2/en_speaker_1` | American | Female |
| `v2/en_speaker_2` | British | Male |
| `v2/en_speaker_3` | British | Female |
| `v2/en_speaker_4` | Australian | Male |
| `v2/en_speaker_5` | Australian | Female |

---

## Bark Special Features

Add emotion to text:
- `[laughter]` — adds laughter
- `[sigh]` — adds a sigh
- `ALL CAPS` — adds emphasis
- `...` — adds pause

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| "No module named bark" | Run `pip install git+https://github.com/suno-ai/bark.git` |
| "No module named scipy" | Run `pip install scipy` |
| Slow generation | First run downloads models — be patient |
| Audio sounds weird | Try a different voice preset |
| "ffmpeg not found" | Run `brew install ffmpeg` |

---

## Files

| File | Description |
|------|-------------|
| `generate_audio_bark.py` | Generation script |
| `audio/*.mp3` | Generated audio files |
| `BARK-NARRATION-GUIDE.md` | This guide |
