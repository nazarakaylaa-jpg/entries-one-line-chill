#!/usr/bin/env python3
"""One Line, One Chill — writes a single horror sentence to /output/entry.txt.

The line: a concrete, specific image (a negative test, a kick synced to a
heartbeat), a scare that is earned by the twist rather than announced, and
a last word that lands the blow. One sentence, well under 200 characters.
"""

import os

ENTRY = "The pregnancy test was negative, but something inside me has started kicking in time with my heartbeat."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    text = ENTRY.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text.count(".") == 1 and text.endswith("."), "entry must be a single sentence"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()
