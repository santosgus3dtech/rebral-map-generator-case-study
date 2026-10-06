from __future__ import annotations

import argparse
import json
from pathlib import Path

from .generator import generate_workbook
from .preview import render_preview


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate a synthetic expense map workbook")
    parser.add_argument("input", type=Path)
    parser.add_argument("output", type=Path)
    parser.add_argument("--preview", type=Path)
    args = parser.parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    generate_workbook(payload, args.output)
    if args.preview:
        render_preview(payload, args.preview)
    print(f"Synthetic workbook generated: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
