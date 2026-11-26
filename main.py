#!/usr/bin/env python3
"""Funniest cat voicemail greeting — program entrypoint (v1 text)."""

import os

LINE = "Hi, it's Mochi. I can't come to the phone, I'm napping. Leave a message after the beep. I'll wake you at 4 AM anyway."


# Mochi the cat answers the phone so you don't have to.
def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
