# Contributing

Contributions are welcome for educational improvements, bug fixes and clearer explanations.

## Guidelines

- Keep notebooks self-contained and runnable.
- Keep comments concise and in English.
- Do not commit private datasets, credentials or local configuration files.
- Prefer public datasets with clear source notes.
- Explain chemistry assumptions and ML limitations clearly.

## Before submitting changes

Run:

```bash
python scripts/check_notebook_syntax.py notebooks
python scripts/scan_repo_safety.py .
```
