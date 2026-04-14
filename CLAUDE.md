# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

`tau-ceti-tracker` is a Python 3.13 project managed with `uv`.

## Commands

```bash
# Run the application
uv run python main.py

# Add a dependency
uv add <package>

# Run tests (once a test suite exists)
uv run pytest

# Run a single test
uv run pytest tests/path/to/test_file.py::test_name
```

## Architecture

The project is in its initial scaffold phase. `main.py` is the entry point containing a `main()` function. As the project grows, structure should be added here.


I'm using this project to improve my python programming. I don't want you to really write code for this project unless I need help. Big goal is for me to learn and understand.