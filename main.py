#!/usr/bin/env python3
"""Five Seconds to Explain the Glass.

Writes the single sentence a house cat would say five seconds after
sweeping a glass off the table, to /output/entry.txt.

The cat's defence, drafted once and spoken in five seconds: the glass
had been empty since breakfast and was squatting in the cat's sunbeam,
so the cat evicted it. No apology, no confession, just cat logic.
"""

import os

# One sentence, spoken in the cat's own voice. The glass is not a
# victim of gravity here: it is a squatter in the sunbeam, and the cat
# is the landlord. Eviction, not an accident.
LINE = (
    "That glass had been empty since breakfast and was squatting in my "
    "sunbeam, so I evicted it \u2014 the floor is where empty things go."
)

MAX_CHARS = 200


def validate(text):
    """Check the line against the gate: one sentence, 1-200 chars."""
    if not text or text.isspace():
        raise ValueError("entry is empty")
    if len(text) > MAX_CHARS:
        raise ValueError("entry is %d chars, over the 200-char cap" % len(text))
    if text.count(".") != 1 or "?" in text or "!" in text:
        raise ValueError("entry must be exactly one sentence")
    return text


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    line = validate(LINE)
    path = os.path.join(out_dir, "entry.txt")
    # No trailing newline: the gate counts every character, so the file
    # holds exactly the sentence and nothing else.
    with open(path, "wb") as fh:
        fh.write(line.encode("utf-8"))
    os.chmod(path, 0o644)
    print("wrote %s (%d chars)" % (path, len(line)))


if __name__ == "__main__":
    main()
