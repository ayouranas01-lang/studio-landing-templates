"""Generate Banner / Pennant pages from the poster image or custom text."""

import math
import tempfile
from pathlib import Path

from PIL import Image
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

from .utils import (
    CODE_FONT,
    CUT_LINE_COLOR,
    CUT_LINE_DASH,
    CUT_LINE_WIDTH,
    MARGIN,
    PAGE_HEIGHT,
    PAGE_WIDTH,
    SUBTITLE_FONT,
    TITLE_FONT,
)


def _draw_pennant_triangle(
    c: Canvas,
    cx: float,
    cy: float,
    width: float,
    height: float,
    fill_image_path: str | None = None,
    letter: str | None = None,
) -> None:
    """Draw a single triangular pennant (point-down) with optional letter."""
    half_w = width / 2

    # Dashed outline
    c.setStrokeColorRGB(*CUT_LINE_COLOR)
    c.setLineWidth(CUT_LINE_WIDTH)
    c.setDash(*CUT_LINE_DASH)

    path = c.beginPath()
    path.moveTo(cx - half_w, cy + height)
    path.lineTo(cx + half_w, cy + height)
    path.lineTo(cx, cy)
    path.close()
    c.drawPath(path, stroke=1, fill=0)
    c.setDash([])

    # Tab at top for hanging
    tab_h = 0.4 * inch
    c.setDash(*CUT_LINE_DASH)
    c.rect(cx - half_w, cy + height, width, tab_h, stroke=1, fill=0)
    c.setDash([])

    # Fold line
    c.setStrokeColorRGB(0.85, 0.85, 0.85)
    c.setLineWidth(0.3)
    c.setDash([2, 2])
    c.line(cx - half_w, cy + height, cx + half_w, cy + height)
    c.setDash([])

    # Letter inside the pennant
    if letter:
        c.setFont(CODE_FONT, 48)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        text_y = cy + height * 0.55
        c.drawCentredString(cx, text_y, letter)


def draw_banner_pennants(
    c: Canvas,
    title: str,
    banner_text: str | None = None,
    full_image: Image.Image | None = None,
) -> None:
    """Draw one or more pages of triangular banner pennants.

    If *banner_text* is provided, each letter becomes a pennant.
    Otherwise, the title is used.
    """
    text = (banner_text or title).upper().replace(" ", "")
    if not text:
        text = "POSTER"

    # Layout: 3 pennants per row, 2 rows per page
    pennant_w = 3.2 * inch
    pennant_h = 4.0 * inch
    per_row = 3
    rows_per_page = 2
    per_page = per_row * rows_per_page

    total_pages = math.ceil(len(text) / per_page)

    for page_idx in range(total_pages):
        # Page header
        c.setFont(TITLE_FONT, 16)
        c.setFillColorRGB(0.15, 0.15, 0.15)
        header_y = PAGE_HEIGHT - MARGIN - 0.4 * inch
        c.drawCentredString(PAGE_WIDTH / 2, header_y, "Banner Pennants")

        if total_pages > 1:
            c.setFont(SUBTITLE_FONT, 10)
            c.setFillColorRGB(0.5, 0.5, 0.5)
            c.drawCentredString(
                PAGE_WIDTH / 2,
                header_y - 0.25 * inch,
                f"Page {page_idx + 1} of {total_pages}",
            )

        start_idx = page_idx * per_page
        letters_on_page = text[start_idx : start_idx + per_page]

        start_y = header_y - 0.7 * inch
        start_x = PAGE_WIDTH / 2 - (per_row * pennant_w) / 2 + pennant_w / 2

        for i, letter in enumerate(letters_on_page):
            row = i // per_row
            col = i % per_row
            cx = start_x + col * pennant_w
            cy = start_y - (row + 1) * (pennant_h + 0.6 * inch)

            _draw_pennant_triangle(c, cx, cy, pennant_w, pennant_h, letter=letter)

        # Footer
        c.setFont(SUBTITLE_FONT, 10)
        c.setFillColorRGB(0.6, 0.6, 0.6)
        c.drawCentredString(
            PAGE_WIDTH / 2,
            MARGIN + 0.3 * inch,
            "Cut along dashed lines. Fold tab and string through.",
        )

        c.showPage()
