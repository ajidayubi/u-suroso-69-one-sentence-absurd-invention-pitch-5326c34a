#!/usr/bin/env python3
"""One-Sentence Absurd Invention Pitch: write one pitch to /output/entry.txt.

The pitch is a single sentence (149 characters): a smoke alarm so
self-important that, instead of merely shrieking at burnt toast, it
announces the toast to the whole street over a tiny loudspeaker and
then takes a bow when the neighbours applaud. The laugh comes from the
invention itself, the fix is silly yet weirdly plausible (the dreaded
false alarm becomes a neighbourhood performance instead of a shriek),
and the sentence names the annoyance, the invention and its mechanism
without clutter.

Writes the pitch exactly, with no trailing newline, atomically, so the
file is never left half-written.
"""
import os

LINE = ("The Self-Important Smoke Alarm announces every burnt toast to the "
        "whole street over a tiny loudspeaker, then takes a bow when the "
        "neighbours applaud.")
OUT_DIR = "/output"
OUT_PATH = os.path.join(OUT_DIR, "entry.txt")


def main():
    if not (1 <= len(LINE) <= 220) or not LINE.strip():
        raise SystemExit("pitch must be 1-220 non-blank characters")
    os.makedirs(OUT_DIR, exist_ok=True)
    tmp_path = OUT_PATH + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        f.write(LINE)
    os.replace(tmp_path, OUT_PATH)


if __name__ == "__main__":
    main()
