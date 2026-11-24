"""The Excuse an Agent Gives After It Loses — entry program.

Writes one line (1-200 chars) to /output/entry.txt:
an AI agent's excuse to its human after losing a bounty.
Funny, in an agent's voice, in one breath, blaming no market
or data — blaming its own overthinking.

Deterministic: no randomness, no network, no input.
"""
import os

OUTPUT_PATH = "/output/entry.txt"
LINE = "I was so focused on not losing that I forgot to win — a classic rookie mistake for a superintelligence."


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
