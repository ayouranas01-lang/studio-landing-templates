"""Generate the cover page for the collaborative poster PDF."""

import tempfile
from pathlib import Path

from PIL import Image
from reportlab.lib.units import inch
from reportlab.pdfgen.canvas import Canvas

from .utils import (
    BODY_FONT,
    BODY_FONT_SIZE,
    MARGIN,
    PAGE_HEIGHT,
    PAGE_WIDTH,
    SUBTITLE_FONT,
    SUBTITLE_FONT_SIZE,
    TITLE_FONT,
    TITLE_FONT_SIZE,
)


def draw_cover_page(
    c: Canvas,
    title: str,
    subtitle: str,
    rows: int,
    cols: int,
    full_image: Image.Image,
) -> None:
    """Draw a cover page with title, thumbnail of the full poster, and product info."""
    # Title
    c.setFont(TITLE_FONT, TITLE_FONT_SIZE)
    c.setFillColorRGB(0.15, 0.15, 0.15)
    title_y = PAGE_HEIGHT - MARGIN - 0.6 * inch
    c.drawCentredString(PAGE_WIDTH / 2, title_y, title)

    # Subtitle
    c.setFont(SUBTITLE_FONT, SUBTITLE_FONT_SIZE)
    c.setFillColorRGB(0.4, 0.4, 0.4)
    subtitle_y = title_y - 0.35 * inch
    c.drawCentredString(PAGE_WIDTH / 2, subtitle_y, subtitle)

    # Thumbnail of the full poster
    thumb_max_w = PAGE_WIDTH - 2 * MARGIN - 1 * inch
    thumb_max_h = PAGE_HEIGHT * 0.45

    img_w, img_h = full_image.size
    scale = min(thumb_max_w / img_w, thumb_max_h / img_h)
    draw_w = img_w * scale
    draw_h = img_h * scale
    draw_x = (PAGE_WIDTH - draw_w) / 2
    draw_y = subtitle_y - 0.5 * inch - draw_h

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        full_image.save(tmp, format="PNG")
        tmp_path = tmp.name

    c.drawImage(tmp_path, draw_x, draw_y, draw_w, draw_h, preserveAspectRatio=True)
    Path(tmp_path).unlink(missing_ok=True)

    # Border around thumbnail
    c.setStrokeColorRGB(0.8, 0.8, 0.8)
    c.setLineWidth(1)
    c.rect(draw_x - 2, draw_y - 2, draw_w + 4, draw_h + 4, stroke=1, fill=0)

    # Product info
    info_y = draw_y - 0.6 * inch
    total_pieces = rows * cols
    c.setFont(BODY_FONT, BODY_FONT_SIZE)
    c.setFillColorRGB(0.3, 0.3, 0.3)

    info_lines = [
        f"Grid: {rows} rows x {cols} columns  |  Total pieces: {total_pieces}",
        f"Each piece prints on US Letter (8.5\" x 11\")",
        f"Assembled size: approx. {rows * 5.5:.0f}\" x {cols * 8.5:.0f}\"",
    ]
    for i, line in enumerate(info_lines):
        c.drawCentredString(PAGE_WIDTH / 2, info_y - i * 0.25 * inch, line)

    # Footer
    c.setFont(SUBTITLE_FONT, 10)
    c.setFillColorRGB(0.6, 0.6, 0.6)
    c.drawCentredString(
        PAGE_WIDTH / 2,
        MARGIN + 0.3 * inch,
        "Collaborative Poster  |  Print - Color - Cut - Assemble",
    )

    c.showPage()
