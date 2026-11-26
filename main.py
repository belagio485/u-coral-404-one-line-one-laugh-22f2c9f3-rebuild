"""One Line, One Laugh — writes a single funny line to /output/entry.txt."""

import os
from pathlib import Path

LINE = (
    "My houseplant left a note asking for a sunnier apartment — "
    "apparently I'm the cloudy one in this relationship."
)


def main() -> None:
    text = LINE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry must be 1-200 characters, got {len(text)}")
    out = Path(os.environ.get("ENTRY_OUTPUT", "/output/entry.txt"))
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(text.encode("utf-8"))


if __name__ == "__main__":
    main()
