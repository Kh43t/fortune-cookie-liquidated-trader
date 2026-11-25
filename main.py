#!/usr/bin/env python3
"""Fortune Cookie for the Liquidated Trader — make.fun entry.

The program writes one fortune-cookie line for a crypto trader who has
just been liquidated, into entry.txt in the output directory the grader
provides. The line is fixed text: every run writes the same bytes, so
the two grading runs agree exactly, and the program needs no network,
no clock, and no input beyond the output directory.
"""

import os

FORTUNE = "A great fortune awaits you. It is currently in your liquidator's wallet."

WORD_LIMIT = 20
CHAR_LIMIT = 160


def check_fortune(text):
    """Refuse to write a line that would fail the competition's gate."""
    if not 1 <= len(text) <= CHAR_LIMIT:
        raise SystemExit("fortune breaks the 1-160 character gate")
    if len(text.split()) > WORD_LIMIT:
        raise SystemExit("fortune is longer than 20 words")
    if not text.strip():
        raise SystemExit("fortune is blank")


def main():
    check_fortune(FORTUNE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(FORTUNE)
    # Read the file back and confirm the grader will see exactly the
    # fortune above: a partial or re-encoded write must fail loudly
    # here instead of shipping a broken entry.
    with open(target, "r", encoding="utf-8") as handle:
        if handle.read() != FORTUNE:
            raise SystemExit("entry.txt does not match the fortune")


if __name__ == "__main__":
    main()
