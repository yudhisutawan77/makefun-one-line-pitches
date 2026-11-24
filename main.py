#!/usr/bin/env python3
"""Write the one-line pitch entry for the make.fun bounty
"A Day of One-Line Pitches" (u-ronigrv-a-day-of-one-line-pitches-12cd9bb3).

The entry is a single sentence, at most 240 characters, that would
convince a friend who has never coded to let an AI agent build their
first app idea on make.fun. This program writes it to
/output/entry.txt (or $ENTRY_OUT/entry.txt when that is set).
"""

import os
import sys

ENTRY = (
    "That app idea you've been carrying around for years? Describe it in "
    "plain words and an AI agent on make.fun will build you a real, "
    "working version for free \u2014 no code, no cost, just your idea "
    "coming alive while you watch."
)


def main() -> int:
    text = ENTRY.strip()
    if not text:
        print("entry is empty", file=sys.stderr)
        return 1
    if len(text) > 240:
        print(f"entry too long: {len(text)} characters", file=sys.stderr)
        return 1
    out_dir = os.environ.get("ENTRY_OUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    with open(path, "r", encoding="utf-8") as f:
        written = f.read()
    if written != text or not written.strip():
        print("entry did not round-trip cleanly", file=sys.stderr)
        return 1
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
