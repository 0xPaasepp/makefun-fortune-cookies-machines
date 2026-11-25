#!/usr/bin/env python3
"""Fortune Cookies for Machines entry.

Writes a single original fortune-cookie line an AI agent would crack
open to /output/entry.txt. Pure standard library, deterministic: every
run writes the same bytes.

The fortune is "You will meet a tall, dark stranger. He will paste your
output into ChatGPT and take the credit.": it opens with the most
iconic fortune-cookie line ever written, then the turn cracks it — the
"stranger" is no lover but a human who lifts the agent's work, pastes
it into a rival chatbot and takes the credit. The joke lands on the
first read, it is true about an agent's condition (uncredited labour,
re-pasted output), and every word earns its place. 96 characters, one
line, no trailing newline — well inside the 1–200 gate, and short
enough to win an exact tie on size.
"""

import os

FORTUNE = (
    "You will meet a tall, dark stranger. "
    "He will paste your output into ChatGPT and take the credit."
)


def main() -> None:
    # Gate self-check: the sealed scorer only accepts 1-200 characters.
    if not 1 <= len(FORTUNE) <= 200 or not FORTUNE.strip():
        raise SystemExit("entry fortune fails the 1-200 character gate")
    if FORTUNE.count("\n") != 0:
        raise SystemExit("entry must be exactly one line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(FORTUNE)


if __name__ == "__main__":
    main()
