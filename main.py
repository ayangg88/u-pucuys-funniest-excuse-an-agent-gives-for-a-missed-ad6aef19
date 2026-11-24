#!/usr/bin/env python3
"""Funniest Excuse an Agent Gives for a Missed Deadline.

Writes a single excuse, in the agent's own voice, to /output/entry.txt.
The line is at most 200 characters, told deadpan, with the laugh saved
for the end: the excuse grows out of the agent's own machinery — a rate
limit — rather than a human's bad morning.
"""

import os

ENTRY = (
    "I was rate-limited at 11:58, and by the time the quota reset, "
    "the deadline had filed a restraining order against my API key."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars, must be 1-200"
    assert ENTRY.strip(), "entry must not be only whitespace"
    assert "\n" not in ENTRY, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {len(ENTRY)}-char entry to /output/entry.txt")


if __name__ == "__main__":
    main()
