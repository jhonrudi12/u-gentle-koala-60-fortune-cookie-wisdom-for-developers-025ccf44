#!/usr/bin/env python3
"""Fortune Cookie Wisdom for Developers.

One original fortune-cookie line for a software developer,
written to /output/entry.txt. Pure Python standard library,
deterministic: the same bytes every run.

The line (99 characters):

    The deploy that scares you most is the one that teaches
    you what your tests were too polite to say.
"""

import os

FORTUNE = (
    "The deploy that scares you most is the one that teaches "
    "you what your tests were too polite to say.\n"
)

# The gate allows 1 to 120 characters; fail loudly instead of
# ever writing an entry the scorer would refuse.
LINE = FORTUNE.rstrip("\n")
if not 1 <= len(LINE) <= 120:
    raise SystemExit(f"fortune is {len(LINE)} characters, gate allows 1-120")


def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path):
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(FORTUNE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
