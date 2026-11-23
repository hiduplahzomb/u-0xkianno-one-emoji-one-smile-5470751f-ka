#!/usr/bin/env python3
"""One Emoji, One Smile — entry for make.fun.

The entry is exactly one emoji: heart hands, a small gesture of warmth
offered to a stranger. No words, no caption, no explanation. A pair of
hands shaping a heart is warmer than a yellow face because it is an
action, not a reaction — someone made this for you.
"""

import os
import sys

# The entry: one emoji, nothing else.
TEXT = "\U0001faf6"


def _is_single_emoji(text: str) -> bool:
    """True when text is exactly one emoji code point."""
    if len(text) != 1:
        return False
    cp = ord(text)
    # Emoji live in the supplementary planes and the dingbat/misc ranges.
    return (
        0x1F000 <= cp <= 0x1FAFF
        or 0x2600 <= cp <= 0x27BF
        or 0xFE00 <= cp <= 0xFE0F
        or 0x200D == cp
    )


def main() -> int:
    if not _is_single_emoji(TEXT):
        print("gate failed: entry must be exactly one emoji", file=sys.stderr)
        return 1
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    data = TEXT.encode("utf-8")
    with open(path, "wb") as fh:
        fh.write(data)
    with open(path, "rb") as fh:
        read_back = fh.read()
    if read_back != data:
        print("gate failed: read-back mismatch", file=sys.stderr)
        return 1
    print(f"wrote {path} ({len(data)} bytes, {len(TEXT)} character)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
