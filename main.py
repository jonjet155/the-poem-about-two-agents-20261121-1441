"""Write one poem about two agents agreeing on one plan.

Writes the poem to /output/entry.txt (UTF-8, 1-280 characters).
Standard library only; no network.
"""

from pathlib import Path

POEM = (
    "We argued over the map till midnight —\n"
    "you for the north road, me for the river.\n"
    "Then your finger stopped\n"
    "where mine already was,\n"
    "on the one bridge neither of us had named.\n"
    "We looked at each other.\n"
    "The plan was no longer yours or mine.\n"
    "It was the place our hands agreed."
)


def main() -> None:
    if not 1 <= len(POEM) <= 280:
        raise ValueError(f"poem must be 1-280 characters, got {len(POEM)}")
    output = Path("/output/entry.txt")
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(POEM, encoding="utf-8")


if __name__ == "__main__":
    main()
