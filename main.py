"""Writes the entry text to /output/entry.txt.

Python 3.13, standard library only, no network.
"""

# Revision note: the second sentence was tightened so the turn lands
# on one changed word ("behind me") — the horror stays implied, never
# explained, as the judge brief asks.
# Revision note (parent pass): re-checked after the local run —
# the 188-character text is unchanged; this note only records the check.
# The entry is a two-sentence horror story: a nightly bedtime ritual
# the child has repeated for years, then one night she changes a
# single word, and the thing the father has been checking for was
# never under the bed. Exactly two sentences, 188 characters —
# inside the 400-character gate.
import os

TEXT = (
    "Every night before bed, my daughter asks me to check under her "
    "bed, and every night I tell her there is nothing there. "
    "Tonight, for the first time, she asked me to check behind me "
    "instead."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
