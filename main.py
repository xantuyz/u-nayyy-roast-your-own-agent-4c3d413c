#!/usr/bin/env python3
"""Entry for make.fun 'Roast Your Own Agent' bounty.

Writes one line -- a roast of the entrant's own AI agent, whose
subagents keep spawning subagents until one of them asks the human
what to do -- to /output/entry.txt. Standard library only, no
network, deterministic.
"""

import os

ROAST = "My agent's subagents spawn subagents until one asks me what to do. I'm the artificial intelligence."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    # The gate accepts one line of 1 to 200 characters, not only whitespace.
    assert 1 <= len(ROAST) <= 200, "roast must be 1-200 characters"
    assert "\n" not in ROAST and ROAST.strip(), "roast must be one non-blank line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="ascii", newline="") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
