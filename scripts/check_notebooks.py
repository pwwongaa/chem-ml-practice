from __future__ import annotations

import ast
import re
from pathlib import Path

import nbformat

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"

LOCAL_PATH_PATTERNS = [
    "/mnt/data",
    "/home/",
    "C:\\Users",
]

FORBIDDEN_TEXT = [
    "Teaching focus",
    "Student practice",
    "Chapter 1",
    "Chapter 2",
    "Chapter 3",
]


def check_code_syntax(source: str, notebook_name: str, cell_index: int) -> list[str]:
    errors = []
    stripped = source.lstrip()
    if stripped.startswith("!") or stripped.startswith("%"):
        return errors
    try:
        ast.parse(source)
    except SyntaxError as exc:
        errors.append(f"{notebook_name} cell {cell_index}: syntax error: {exc}")
    return errors


def main() -> None:
    errors = []
    notebook_paths = sorted(NOTEBOOK_DIR.glob("*.ipynb"))

    if len(notebook_paths) != 5:
        errors.append(f"Expected 5 notebooks, found {len(notebook_paths)}")

    for path in notebook_paths:
        nb = nbformat.read(path, as_version=4)
        full_text = "\n".join(cell.get("source", "") for cell in nb.cells)

        for pattern in LOCAL_PATH_PATTERNS:
            if pattern in full_text:
                errors.append(f"{path.name}: local path pattern found: {pattern}")

        for phrase in FORBIDDEN_TEXT:
            if phrase in full_text:
                errors.append(f"{path.name}: unwanted phrase found: {phrase}")

        if "Exercise" in full_text and "Answer" not in full_text:
            errors.append(f"{path.name}: exercises found but answer sections missing")

        for index, cell in enumerate(nb.cells):
            if cell.cell_type != "code":
                continue
            errors.extend(check_code_syntax(cell.source, path.name, index))

    if errors:
        print("Notebook checks failed:\n")
        for error in errors:
            print("-", error)
        raise SystemExit(1)

    print(f"Notebook checks passed for {len(notebook_paths)} notebooks.")


if __name__ == "__main__":
    main()
