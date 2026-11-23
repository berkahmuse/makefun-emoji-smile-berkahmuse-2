#!/usr/bin/env python3
"""One Emoji, One Smile - entry for @berkahmuse-2.

Writes exactly one emoji, U+1FAF6 HEART HANDS, to /output/entry.txt:
two hands shaping a heart - a warm, open gesture of affection
offered to a stranger: kind, friendly, gently funny, universal,
and clearly chosen rather than the default smiley.
"""
import os

EMOJI = "\U0001FAF6"  # 🫶 Heart Hands

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)

if __name__ == "__main__":
    main()
