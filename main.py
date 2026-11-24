#!/usr/bin/env python3
"""One Word From Your Ex — make.fun bounty entry.

Writes exactly one word to /output/entry.txt: the word an ex would use
to describe the entrant.

The word is "placeholder": the most painfully honest one-word verdict
an ex can deliver. It lands instantly — no explanation needed — because
everyone has either been one or dated one. It is funny through the sharp
turn it takes (you thought you were the one; you were a placeholder),
and it stings because it is true and the entrant plainly knows it.

Rules compliance (see RULES.txt in the competition kit):
- /output/entry.txt must be UTF-8 text of 1 to 24 characters, not only
  white space, holding exactly one word and nothing else.
- Standard library only: no third-party imports, so the grader can run
  this anywhere with a plain Python 3.
- The output file is written with plain open() and then chmod 644, so
  the grader (running as a different user) can read it. Never use
  tempfile.mkstemp here: it forces mode 0600 and the grader cannot
  read the result.

Run: python3 main.py
"""

import os

WORD = "placeholder"

OUTPUT_PATH = "/output/entry.txt"

# The gate allows 1 to 24 characters of UTF-8 text, not only white space.
MAX_LENGTH = 24


def validate(word):
    """Check the entry is exactly one word within the gate's limits.

    The gate rejects anything that is not a single word: empty text,
    anything over 24 characters, non-letters, or any whitespace inside
    the word. A lone word with no spaces passes all four checks.
    """
    if not word or len(word) > MAX_LENGTH:
        raise ValueError("entry must be 1 to 24 characters")
    if not word.isalpha():
        raise ValueError("entry must be exactly one word of letters")
    if word.strip() != word or " " in word:
        raise ValueError("entry must be a single word with no spaces")
    return word


def main():
    word = validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(word + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
