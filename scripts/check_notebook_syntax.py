#!/usr/bin/env python3
"""Syntax-check code cells in Jupyter notebooks."""

from __future__ import annotations

import ast
import json
import sys
from pathlib import Path


def clean_notebook_code(code: str) -> str:
    """Remove notebook shell/magic lines before AST parsing."""
    lines = []
    for line in code.splitlines():
        stripped = line.lstrip()
        if stripped.startswith("!") or stripped.startswith("%"):
            continue
        lines.append(line)
    return "\n".join(lines)


def check_notebook(path: Path) -> list[str]:
    errors = []
    nb = json.loads(path.read_text(encoding="utf-8"))
    for idx, cell in enumerate(nb.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue
        code = "".join(cell.get("source", []))
        try:
            ast.parse(clean_notebook_code(code))
        except SyntaxError as exc:
            errors.append(f"{path}: cell {idx}: {exc}")
    return errors


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("notebooks")
    notebooks = sorted(root.rglob("*.ipynb")) if root.is_dir() else [root]
    all_errors = []
    for notebook in notebooks:
        all_errors.extend(check_notebook(notebook))
    if all_errors:
        print("Notebook syntax errors found:")
        for error in all_errors:
            print("-", error)
        return 1
    print(f"Notebook syntax check passed for {len(notebooks)} notebook(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
