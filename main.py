#!/usr/bin/env python3
"""The One-Liner Groan-Off entry.

Writes one original one-line dad joke to /output/entry.txt.
Standard library only; fully deterministic: the same line every run.

The joke was picked from three drafts with the write-humor linter
(all three clean); this one won because the pun lands on the very
last word, the setup is one short question, and nothing after the
punchline dilutes it.
"""

import os

JOKE = (
    "I asked my fridge why it was so cold to me. "
    "It said, \"I'm just chilling \u2014 take it or leftovers.\""
)

# The sealed gate: /output/entry.txt must be UTF-8 text of 1 to 140
# characters, not only white space.
MIN_CHARS = 1
MAX_CHARS = 140


def main():
    line = JOKE.strip()
    if not (MIN_CHARS <= len(line) <= MAX_CHARS) or not line.strip():
        raise SystemExit("joke fails the 1-140 character gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
