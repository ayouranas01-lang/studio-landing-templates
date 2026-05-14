#!/usr/bin/env python3
"""Package the Collaborative Poster Generator project into a distributable ZIP."""

import shutil
import sys
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
DIST_DIR = PROJECT_DIR / "dist"
ARCHIVE_NAME = "collaborative-poster-generator"

INCLUDE_FILES = [
    "main.py",
    "package.py",
    "requirements.txt",
    "README.md",
    "GUIDE_AR.md",
    "GUIDE_EN.md",
    ".gitignore",
]

INCLUDE_DIRS = [
    "poster_generator",
]

CREATE_DIRS = [
    "input",
]


def main() -> None:
    """Build the distributable archive."""
    staging = DIST_DIR / ARCHIVE_NAME
    if staging.exists():
        shutil.rmtree(staging)
    staging.mkdir(parents=True)

    for fname in INCLUDE_FILES:
        src = PROJECT_DIR / fname
        if src.exists():
            shutil.copy2(src, staging / fname)

    for dname in INCLUDE_DIRS:
        src = PROJECT_DIR / dname
        if src.is_dir():
            shutil.copytree(src, staging / dname, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))

    for dname in CREATE_DIRS:
        (staging / dname).mkdir(exist_ok=True)
        (staging / dname / ".gitkeep").touch()

    archive_path = shutil.make_archive(str(DIST_DIR / ARCHIVE_NAME), "zip", root_dir=DIST_DIR, base_dir=ARCHIVE_NAME)

    shutil.rmtree(staging)

    print(f"Package created: {archive_path}")
    print(f"Size: {Path(archive_path).stat().st_size / 1024:.1f} KB")


if __name__ == "__main__":
    main()
