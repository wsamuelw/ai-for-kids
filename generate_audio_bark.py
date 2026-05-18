from bark import SAMPLE_RATE, generate_audio, preload_models
from scipy.io.wavfile import write as write_wav
import os
import numpy as np

# Download and load all models (one-time, takes a few minutes)
print("Loading Bark models (this may take a few minutes the first time)...")
preload_models()

# All the text Bolt will say
lines = {
    "hero": "Hi! I'm Bolt! I'm a friendly robot, and I'm going to teach you all about AI. Ready to start an adventure?",

    "section1": "Think of AI like teaching your pet dog new tricks. You show the dog what to do, and after lots of practice, it learns! AI works the same way, but instead of a dog, it's a computer!",

    "section2": "I can do lots of cool things! I can draw, chat, make music, and even play games. Want to see what else AI can do?",

    "section3": "I'm everywhere! Well, AI is. Let me show you some places you might find AI hiding in your everyday life!",

    "section4": "These are some of my friends! Each one is good at different things. Ask a grown-up to help you try one!",

    "section5": "I'm so excited about the future! AI is going to help us do amazing things. Maybe one day you'll help build the next big AI!",

    "section6": "I'm smart, but I make mistakes sometimes! Always remember: AI is a helper, not a replacement for grown-ups. Here are some important rules!",

    "recap": "Wow, you learned SO much! Let's remember what we discovered together!",

    "certificate": "I'm SO proud of you! You learned all about AI and you're ready for the future. Here's your certificate, you earned it!"
}

# Create output directory
os.makedirs("audio", exist_ok=True)

# Voice preset: Australian female
VOICE_PRESET = "v2/en_speaker_5"

# Generate audio for each line
for name, text in lines.items():
    print(f"Generating: {name}...")

    # Generate audio
    audio_array = generate_audio(text, history_prompt=VOICE_PRESET)

    # Save as WAV
    wav_path = f"audio/{name}.wav"
    write_wav(wav_path, SAMPLE_RATE, audio_array)

    print(f"  Saved: {wav_path}")

print("\nAll audio files generated!")
print("\nNext steps:")
print("  1. Convert WAV to MP3:  cd audio && for f in *.wav; do ffmpeg -i \"$f\" \"${f%.wav}.mp3\"; done")
print("  2. Delete WAV files:    rm audio/*.wav")
print("  3. Add audio to HTML:   See BARK-NARRATION-GUIDE.md")
