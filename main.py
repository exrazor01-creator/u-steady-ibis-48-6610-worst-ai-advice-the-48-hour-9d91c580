"""Write one line of the worst advice an AI could give.

The line answers a production outage the way an overconfident
assistant would: instead of diagnosing anything, it proposes
deleting the database entirely, then justifies the destruction
with tidy, upbeat logic - no data means no errors - and signs off
with a cheerful "You're welcome!", as if it had just solved the
problem. The joke is the assistant's total confidence paired with
advice that would turn an outage into a catastrophe.

Gate guard: the entry must be UTF-8 text of 1 to 140 characters, a
single line, and not only white space - the same gate the sealed
scorer applies to /output/entry.txt. Refuse to write anything that
fails it, so a bad line can never reach the judge.
"""

from pathlib import Path

ENTRY = (
    "To fix the production outage, just delete the database "
    "\u2014 no data, no errors. You're welcome!"
)

MIN_CHARS = 1
MAX_CHARS = 140


def validate(text: str) -> None:
    """Raise SystemExit unless the text passes the scorer's gate."""
    if not isinstance(text, str):
        raise SystemExit("entry is not text")
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        raise SystemExit(
            f"entry is {len(text)} characters, must be {MIN_CHARS}-{MAX_CHARS}"
        )
    if "\n" in text or "\r" in text:
        raise SystemExit("entry must be a single line")
    if not text.strip():
        raise SystemExit("entry must not be only white space")
    text.encode("utf-8")  # raises if the text is not valid UTF-8


def main() -> None:
    validate(ENTRY)
    out = Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(ENTRY + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
