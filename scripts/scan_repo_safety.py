#!/usr/bin/env python3
"""Lightweight repository safety scan for accidental secrets and local paths."""

from __future__ import annotations

import re
import sys
from pathlib import Path

SECRET_PATTERNS = [
    re.compile(r"(?i)api[_-]?key\s*[=:]\s*['\"]?[A-Za-z0-9_\-]{16,}"),
    re.compile(r"(?i)(secret|password|token)\s*[=:]\s*['\"]?[A-Za-z0-9_\-]{12,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"-----BEGIN (RSA|DSA|EC|OPENSSH)? ?PRIVATE KEY-----"),
]

LOCAL_PATH_PATTERNS = [
    re.compile(r"/mnt/data"),
    re.compile(r"/home/[^\s'\"]+"),
    re.compile(r"/Users/[^\s'\"]+"),
    re.compile(r"/content/[^\s'\"]+"),
    re.compile(r"/kaggle/[^\s'\"]+"),
]

SKIP_DIRS = {".git", ".venv", "venv", "env", "__pycache__", ".ipynb_checkpoints"}
TEXT_SUFFIXES = {".py", ".md", ".txt", ".yml", ".yaml", ".json", ".ipynb", ".csv", ".cff", ".gitignore", ".gitattributes"}
ALLOWLIST_FILES = {"scripts/scan_repo_safety.py", "docs/VALIDATION.md"}


def is_text_file(path: Path) -> bool:
    return path.suffix in TEXT_SUFFIXES or path.name in {"LICENSE", "README.md", ".gitignore", ".gitattributes"}


def main() -> int:
    root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path(".")
    findings = []
    for path in root.rglob("*"):
        rel = path.relative_to(root).as_posix() if path.is_relative_to(root) else str(path)
        if rel in ALLOWLIST_FILES:
            continue
        if any(part in SKIP_DIRS for part in path.parts):
            continue
        if not path.is_file() or not is_text_file(path):
            continue
        try:
            text = path.read_text(encoding="utf-8", errors="ignore")
        except Exception:
            continue
        for pattern in SECRET_PATTERNS:
            if pattern.search(text):
                findings.append(f"Possible secret pattern in {path}")
        for pattern in LOCAL_PATH_PATTERNS:
            if pattern.search(text):
                findings.append(f"Possible local path in {path}")
    if findings:
        print("Safety scan findings:")
        for finding in findings:
            print("-", finding)
        return 1
    print("Safety scan passed: no common secret or local path patterns found.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
