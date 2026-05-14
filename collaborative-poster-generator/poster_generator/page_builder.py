"""Build individual PDF pages for each poster piece with cutting lines and code."""

import io
import tempfile
from pathlib import Path

from PIL import Image
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

from .utils import (
    BLEED,
    CODE_FONT,
    CODE_FONT_SIZE,
    CROP_MARK_COLOR,
    CROP_MARK_LENGTH,
    CROP_MARK_WIDTH,
    CUT_LINE_COLOR,
    CUT_LINE_DASH,
    CUT_LINE_WIDTH,
    MARGIN,
    PAGE_HEIGHT,
    PAGE_WIDTH,
)


def _draw_crop_marks(c: Canvas, x: float, y: float, w: float, h: float) -> None:
    """Draw crop marks at the four corners of the content area."""
    c.setStrokeColorRGB(*CROP_MARK_COLOR)
    c.setLineWidth(CROP_MARK_WIDTH)

    corners = [
        (x, y),                # bottom-left
        (x + w, y),            # bottom-right
        (x, y + h),            # top-left
        (x + w, y + h),        # top-right
    ]

    for cx, cy in corners:
        # Horizontal marks
        if cx == x:
            c.line(cx - CROP_MARK_LENGTH, cy, cx - 4, cy)
        else:
            c.line(cx + 4, cy, cx + CROP_MARK_LENGTH, cy)
        # Vertical marks
        if cy == y:
            c.line(cx, cy - CROP_MARK_LENGTH, cx, cy - 4)
        else:
            c.line(cx, cy + 4, cx, cy + CROP_MARK_LENGTH)


def _draw_cutting_lines(c: Canvas, x: float, y: float, w: float, h: float) -> None:
    """Draw dashed cutting lines around the content area."""
    c.setStrokeColorRGB(*CUT_LINE_COLOR)
    c.setLineWidth(CUT_LINE_WIDTH)
    c.setDash(*CUT_LINE_DASH)
    c.rect(x, y, w, h, stroke=1, fill=0)
    c.setDash([])


def _draw_code_label(c: Canvas, code: str, x: float, y: float) -> None:
    """Draw the piece code (e.g. 'A1') at the given position."""
    c.setFont(CODE_FONT, CODE_FONT_SIZE)
    c.setFillColorRGB(0.3, 0.3, 0.3)
    c.drawString(x, y, code)


def draw_piece_page(c: Canvas, piece_image: Image.Image, code: str) -> None:
    """Draw a single poster-piece page onto *c* (a ReportLab Canvas).

    The piece image is centered on the page, surrounded by dashed cutting
    lines, crop marks in the corners, and a code label.
    """
    content_w = PAGE_WIDTH - 2 * MARGIN
    content_h = PAGE_HEIGHT - 2 * MARGIN - 0.4 * inch  # leave room for code

    img_w, img_h = piece_image.size
    scale = min(content_w / img_w, content_h / img_h)
    draw_w = img_w * scale
    draw_h = img_h * scale

    # Center the image
    draw_x = (PAGE_WIDTH - draw_w) / 2
    draw_y = MARGIN + 0.4 * inch + (content_h - draw_h) / 2

    # Save piece image to a temp file for ReportLab
    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        piece_image.save(tmp, format="PNG")
        tmp_path = tmp.name

    c.drawImage(tmp_path, draw_x, draw_y, draw_w, draw_h, preserveAspectRatio=True)

    # Cutting lines around the image area
    cut_x = draw_x - BLEED
    cut_y = draw_y - BLEED
    cut_w = draw_w + 2 * BLEED
    cut_h = draw_h + 2 * BLEED
    _draw_cutting_lines(c, cut_x, cut_y, cut_w, cut_h)

    # Crop marks
    _draw_crop_marks(c, cut_x, cut_y, cut_w, cut_h)

    # Code label (bottom-right of the page)
    _draw_code_label(c, code, PAGE_WIDTH - MARGIN - 0.5 * inch, MARGIN + 0.1 * inch)

    # Clean up temp file
    Path(tmp_path).unlink(missing_ok=True)

    c.showPage()
