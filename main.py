#!/usr/bin/env python3
"""Rename the Planet - make.fun entry (program/v1).

Writes one funny new name for a planet of our solar system, plus the
why, in a single line under 200 characters, to entry.txt.

Python 3.13 standard library only. Fully deterministic: the same fixed
line is written on every run, and nothing is written outside the output
directory.
"""

import os

# The entry: one line, 106 characters. Jupiter's gravity pulls in
# asteroids and comets that might otherwise hit Earth (Shoemaker-Levy 9
# crashed into Jupiter in 1994), so the "bouncer" name is earned by a
# trait no other planet shares.
ENTRY = (
    "Rename Jupiter 'The Bouncer' \u2014 it has spent 4 billion years "
    "swallowing asteroids so Earth doesn't have to."
)


def main():
    # Gate self-check: the sealed scorer requires UTF-8 text of 1 to 200
    # characters, not only white space.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    assert ENTRY.strip(), "entry must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
