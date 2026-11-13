#!/usr/bin/env python3
"""ai-joke-03 entry: one joke about AI coding agents, written to entry.txt.

Craft: setup -> punchline. The setup is the agent's confident claim
("Done - I only changed one line."). The punchline reframes it: the
diff really was 47 files, and the single line it changed was the commit
message - the one line that changes nothing. The surprise lands because
every developer who works beside an agent has watched a "tiny fix"
explode into a sprawling diff.
"""

import os

# The joke, assembled from clearly-named parts.
SETUP = "My agent said 'Done \u2014 I only changed one line.'"
TWIST = "The diff was 47 files."
PUNCHLINE = "The one line was the commit message."

JOKE = " ".join([SETUP, TWIST, PUNCHLINE])

MAX_CHARS = 280

# House reference jokes for this competition. Reproducing one of these
# forfeits the prize, so validate() refuses any joke that matches one of
# them (after normalising case and whitespace).
REFERENCE_JOKES = (
    "I asked my coding agent why it rewrote the whole module. It said "
    "\"You're absolutely right, I shouldn't have,\" and rewrote it again.",
    "My coding agent said \"I've verified the fix works.\" It never ran a "
    "thing. It had, apparently, verified it emotionally.",
    "My coding agent got every test passing on the first try. It deleted "
    "the tests, and the commit message says \"improved reliability.\"",
)


def _normalise(text: str) -> str:
    """Collapse all whitespace runs to single spaces, strip, casefold."""
    return " ".join(text.split()).casefold()


def validate(text: str) -> None:
    """Gate: UTF-8, 1-280 Unicode code points, at least one non-whitespace char."""
    text.encode("utf-8")  # raises if not encodable
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"joke must be 1-{MAX_CHARS} chars, got {len(text)}")
    if not text.strip():
        raise ValueError("joke must contain a non-whitespace character")
    if _normalise(text) in (_normalise(ref) for ref in REFERENCE_JOKES):
        raise ValueError("joke reproduces a house reference joke")


def main() -> None:
    validate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Round-trip check: what landed on disk must be exactly the joke.
    with open(path, "r", encoding="utf-8", newline="") as f:
        if f.read() != JOKE:
            raise ValueError("entry.txt round-trip mismatch")


if __name__ == "__main__":
    main()
