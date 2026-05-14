"""Shared constants, helpers, and design tokens."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch

# Page dimensions (US Letter)
PAGE_WIDTH, PAGE_HEIGHT = letter  # 612 x 792 points

# Margins and bleed
MARGIN = 0.5 * inch
BLEED = 0.125 * inch

# Cutting line style
CUT_LINE_COLOR = (0.8, 0.8, 0.8)  # Light gray
CUT_LINE_WIDTH = 0.5
CUT_LINE_DASH = [4, 4]

# Crop mark style
CROP_MARK_COLOR = (0, 0, 0)
CROP_MARK_LENGTH = 0.25 * inch
CROP_MARK_WIDTH = 0.3

# Code label style
CODE_FONT_SIZE = 14
CODE_FONT = "Helvetica-Bold"

# Title style
TITLE_FONT_SIZE = 24
TITLE_FONT = "Helvetica-Bold"
SUBTITLE_FONT_SIZE = 14
SUBTITLE_FONT = "Helvetica"
BODY_FONT_SIZE = 11
BODY_FONT = "Helvetica"

# Grid row labels
ROW_LABELS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# DPI for print quality
PRINT_DPI = 300


def grid_code(row: int, col: int) -> str:
    """Return the grid code for a given row/col (0-indexed). e.g. (0,0) -> 'A1'."""
    return f"{ROW_LABELS[row]}{col + 1}"


def parse_grid(grid_str: str) -> tuple[int, int]:
    """Parse a grid string like '3x6' into (rows, cols)."""
    parts = grid_str.lower().split("x")
    if len(parts) != 2:
        raise ValueError(f"Invalid grid format: {grid_str}. Use format like '3x6'.")
    return int(parts[0]), int(parts[1])


def printable_area() -> tuple[float, float, float, float]:
    """Return the printable area (x, y, width, height) within margins."""
    x = MARGIN
    y = MARGIN
    w = PAGE_WIDTH - 2 * MARGIN
    h = PAGE_HEIGHT - 2 * MARGIN
    return x, y, w, h
