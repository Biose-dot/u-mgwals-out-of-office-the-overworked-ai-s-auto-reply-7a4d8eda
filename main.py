#!/usr/bin/env python3
"""Out-of-Office: The Overworked AI's Auto-Reply - make.fun entry.

Writes one out-of-office auto-reply (no trailing newline) to
/output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
Deterministic, stdlib only, no network.
"""
import os

ENTRY = "I'm on vacation until Monday. My auto-reply quit after 40,000 unread emails, so for urgent matters please shout into the void - it answers faster than I did."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
