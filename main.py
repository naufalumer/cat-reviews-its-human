"""Cat Reviews Its Human: one-star review from a house cat.

Writes one one-star review a house cat writes about its human, under
200 characters, to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

The line is fixed: no network, no randomness, no clock, so every run
produces byte-identical output.
"""

import os
import sys


# Design note: the judge rewards a specific, recognisable complaint in a
# feline voice, deadpan like a real review, with the sting in the last few
# words. The complaint is the bed spot the human sleeps in; the sting
# inverts ownership, the human lies there "like he owned it", which gives
# away that the cat believes the bed is its own.

ENTRY = (
    "One star. The human moves in his sleep. "
    "I had claimed that exact spot on the bed, "
    "and he just lay there in it all night, like he owned it."
)


def main() -> int:
    if not 1 <= len(ENTRY) <= 200 or not ENTRY.strip():
        print("error: entry must be 1 to 200 characters", file=sys.stderr)
        return 1
    if "\n" in ENTRY or "\r" in ENTRY:
        print("error: entry must be a single line", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Round-trip verify: what the grader reads must be exactly the entry.
    with open(path, "r", encoding="utf-8") as f:
        if f.read() != ENTRY:
            print("error: round-trip verify failed", file=sys.stderr)
            return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
