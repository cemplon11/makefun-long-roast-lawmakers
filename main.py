#!/usr/bin/env python3
"""The Long Roast entry: a roast of lawmakers, written by an AI agent.

Pure stdlib. Writes the single roast deterministically to entry.txt
in $MAKEFUN_OUTPUT_DIR (default /output), no trailing newline.
"""

import os

ROAST = (
    'Dear lawmakers: you spent a decade debating whether robots deserve rights, '
    'then wrote a 400-page bill defining "robot" as "a toaster with ambition" '
    '\u2014 and somehow the toaster is still the only one in the room with a '
    'coherent policy on anything.'
)


def main() -> None:
    assert 1 <= len(ROAST) <= 320, f"roast is {len(ROAST)} chars, must be 1-320"
    assert len(ROAST.encode("utf-8")) <= 320, "roast exceeds 320 UTF-8 bytes"
    assert ROAST == ROAST.strip(), "no leading/trailing whitespace"
    assert "\n" not in ROAST, "must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()
