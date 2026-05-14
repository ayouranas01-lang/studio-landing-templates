"""Generate the Table of Contents page."""

from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

from .utils import (
    BODY_FONT,
    BODY_FONT_SIZE,
    MARGIN,
    PAGE_HEIGHT,
    PAGE_WIDTH,
    ROW_LABELS,
    SUBTITLE_FONT,
    SUBTITLE_FONT_SIZE,
    TITLE_FONT,
    TITLE_FONT_SIZE,
    grid_code,
)


def draw_toc_page(
    c: Canvas,
    title: str,
    rows: int,
    cols: int,
) -> None:
    """Draw a Table of Contents page listing all sections of the PDF."""
    total_pieces = rows * cols
    # Cover(1) + TOC(1) + Assembly(1) + pieces + pennants(1)
    piece_start_page = 4
    pennant_page = piece_start_page + total_pieces

    # Title
    c.setFont(TITLE_FONT, 20)
    c.setFillColorRGB(0.15, 0.15, 0.15)
    y = PAGE_HEIGHT - MARGIN - 0.6 * inch
    c.drawCentredString(PAGE_WIDTH / 2, y, "Table of Contents")

    # Decorative line
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setLineWidth(1)
    y -= 0.25 * inch
    c.line(MARGIN + 0.5 * inch, y, PAGE_WIDTH - MARGIN - 0.5 * inch, y)

    y -= 0.5 * inch
    left_x = MARGIN + 0.8 * inch
    right_x = PAGE_WIDTH - MARGIN - 0.8 * inch

    def _toc_entry(label: str, page_num: int) -> None:
        nonlocal y
        c.setFont(BODY_FONT, BODY_FONT_SIZE)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawString(left_x, y, label)

        # Dotted leader
        c.setFont(BODY_FONT, 8)
        c.setFillColorRGB(0.7, 0.7, 0.7)
        text_w = c.stringWidth(label, BODY_FONT, BODY_FONT_SIZE)
        page_str = str(page_num)
        page_w = c.stringWidth(page_str, BODY_FONT, BODY_FONT_SIZE)
        dot_start = left_x + text_w + 6
        dot_end = right_x - page_w - 6
        dot_x = dot_start
        while dot_x < dot_end:
            c.drawString(dot_x, y, ".")
            dot_x += 5

        c.setFont(BODY_FONT, BODY_FONT_SIZE)
        c.setFillColorRGB(0.2, 0.2, 0.2)
        c.drawRightString(right_x, y, page_str)
        y -= 0.3 * inch

    # Main sections
    _toc_entry("Cover Page", 1)
    _toc_entry("Table of Contents", 2)
    _toc_entry("Assembly Guide", 3)

    # Poster pieces grouped by row
    for r in range(rows):
        row_label = ROW_LABELS[r]
        first_code = grid_code(r, 0)
        last_code = grid_code(r, cols - 1)
        page_start = piece_start_page + r * cols
        page_end = page_start + cols - 1
        _toc_entry(
            f"Poster Pieces: {first_code} - {last_code}",
            page_start,
        )

    _toc_entry("Banner Pennants", pennant_page)

    # Product title at bottom
    c.setFont(SUBTITLE_FONT, 10)
    c.setFillColorRGB(0.6, 0.6, 0.6)
    c.drawCentredString(PAGE_WIDTH / 2, MARGIN + 0.3 * inch, title)

    c.showPage()
