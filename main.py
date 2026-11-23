#!/usr/bin/env python3
"""One Emoji, One Smile - entry for @berkahmuse-2.

Writes exactly one emoji, U+1F917 HUGGING FACE, to /output/entry.txt:
a warm hug offered to a stranger - kind, friendly, gently funny,
universal, and clearly chosen rather than the default smiley.
"""
import os

EMOJI = "\U0001F917"  # 🤗 Hugging Face

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)

if __name__ == "__main__":
    main()
