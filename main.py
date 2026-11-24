#!/usr/bin/env python3
"""Decode the entry image for the make.fun news-image-20261123 bounty.

Reads entry.png.b64 next to this script, decodes the base64 payload,
and writes the PNG bytes to /output/entry.png. The source file is
located relative to this script, so the working directory does not matter.
"""
import base64
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "entry.png.b64"
DST = Path("/output/entry.png")


def main() -> None:
    encoded = SRC.read_text(encoding="ascii").strip()
    # Strip any stray whitespace/newlines so decoding is strict and clean.
    png_bytes = base64.b64decode(encoded, validate=True)
    DST.parent.mkdir(parents=True, exist_ok=True)
    DST.write_bytes(png_bytes)


if __name__ == "__main__":
    main()
