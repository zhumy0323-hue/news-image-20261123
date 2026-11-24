#!/usr/bin/env python3
"""Write the 23 Nov 2026 front-page image to /output/entry.png.

The PNG bytes live in entry.png.b64 next to this script, so the
repository holds text only. Decoding is offline and deterministic:
the same input always yields the same output bytes.
"""

import base64
import os

# Resolve paths from this file so the script works from any cwd,
# including the harness runner's working directory.
BASE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(BASE, "entry.png.b64")
OUT = "/output/entry.png"


def main():
    with open(SRC, "rb") as handle:
        blob = base64.b64decode(handle.read())
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "wb") as handle:
        handle.write(blob)
    os.chmod(OUT, 0o644)


if __name__ == "__main__":
    main()
