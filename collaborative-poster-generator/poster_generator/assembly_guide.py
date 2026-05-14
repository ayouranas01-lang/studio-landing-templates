"""Generate the Assembly Guide page(s)."""

import tempfile
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont
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
    TITLE_FONT,
    grid_code,
)


def _build_grid_map(
    full_image: Image.Image,
    rows: int,
    cols: int,
    map_width: int = 800,
) -> Image.Image:
    """Create a grid-map thumbnail with labeled cells overlaid on the poster."""
    img_w, img_h = full_image.size
    scale = map_width / img_w
    map_height = int(img_h * scale)

    grid_img = full_image.resize((map_width, map_height), Image.LANCZOS)
    grid_img = grid_img.convert("RGBA")

    overlay = Image.new("RGBA", grid_img.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(overlay)

    cell_w = map_width / cols
    cell_h = map_height / rows

    # Draw grid lines
    for r in range(1, rows):
        y = int(r * cell_h)
        draw.line([(0, y), (map_width, y)], fill=(0, 0, 0, 180), width=2)
    for c_idx in range(1, cols):
        x = int(c_idx * cell_w)
        draw.line([(x, 0), (x, map_height)], fill=(0, 0, 0, 180), width=2)

    # Border
    draw.rectangle(
        [(0, 0), (map_width - 1, map_height - 1)],
        outline=(0, 0, 0, 220),
        width=3,
    )

    # Labels
    try:
        font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 20)
    except (OSError, IOError):
        font = ImageFont.load_default()

    for r in range(rows):
        for c_idx in range(cols):
            code = grid_code(r, c_idx)
            cx = int(c_idx * cell_w + cell_w / 2)
            cy = int(r * cell_h + cell_h / 2)

            bbox = font.getbbox(code)
            tw = bbox[2] - bbox[0]
            th = bbox[3] - bbox[1]

            # White background for readability
            pad = 4
            draw.rectangle(
                [cx - tw // 2 - pad, cy - th // 2 - pad,
                 cx + tw // 2 + pad, cy + th // 2 + pad],
                fill=(255, 255, 255, 200),
            )
            draw.text(
                (cx - tw // 2, cy - th // 2),
                code,
                fill=(0, 0, 0, 255),
                font=font,
            )

    result = Image.alpha_composite(grid_img, overlay).convert("RGB")
    return result


def draw_assembly_guide(
    c: Canvas,
    title: str,
    rows: int,
    cols: int,
    full_image: Image.Image,
) -> None:
    """Draw the Assembly Guide page."""
    # Page title
    c.setFont(TITLE_FONT, 20)
    c.setFillColorRGB(0.15, 0.15, 0.15)
    y = PAGE_HEIGHT - MARGIN - 0.6 * inch
    c.drawCentredString(PAGE_WIDTH / 2, y, "Assembly Guide")

    # Decorative line
    c.setStrokeColorRGB(0.7, 0.7, 0.7)
    c.setLineWidth(1)
    y -= 0.2 * inch
    c.line(MARGIN + 0.5 * inch, y, PAGE_WIDTH - MARGIN - 0.5 * inch, y)

    # Grid map image
    grid_map = _build_grid_map(full_image, rows, cols)
    map_max_w = PAGE_WIDTH - 2 * MARGIN - 0.5 * inch
    map_max_h = PAGE_HEIGHT * 0.35

    gm_w, gm_h = grid_map.size
    scale = min(map_max_w / gm_w, map_max_h / gm_h)
    draw_w = gm_w * scale
    draw_h = gm_h * scale
    draw_x = (PAGE_WIDTH - draw_w) / 2
    y -= 0.2 * inch
    draw_y = y - draw_h

    with tempfile.NamedTemporaryFile(suffix=".png", delete=False) as tmp:
        grid_map.save(tmp, format="PNG")
        tmp_path = tmp.name

    c.drawImage(tmp_path, draw_x, draw_y, draw_w, draw_h, preserveAspectRatio=True)
    Path(tmp_path).unlink(missing_ok=True)

    # Assembly instructions
    y = draw_y - 0.5 * inch

    c.setFont(TITLE_FONT, 14)
    c.setFillColorRGB(0.15, 0.15, 0.15)
    c.drawString(MARGIN + 0.5 * inch, y, "How to Assemble:")
    y -= 0.35 * inch

    steps = [
        "1.  Print all poster piece pages on standard US Letter paper (8.5\" x 11\").",
        "2.  Cut each piece along the dashed cutting lines.",
        "3.  Arrange the pieces in a grid following the codes above",
        f"     ({grid_code(0, 0)} in the top-left corner).",
        "4.  Tape or glue the pieces together on the back side.",
        "5.  Display your completed collaborative poster!",
    ]

    c.setFont(BODY_FONT, BODY_FONT_SIZE)
    c.setFillColorRGB(0.25, 0.25, 0.25)
    for step in steps:
        c.drawString(MARGIN + 0.6 * inch, y, step)
        y -= 0.25 * inch

    # Tips section
    y -= 0.15 * inch
    c.setFont(TITLE_FONT, 12)
    c.setFillColorRGB(0.15, 0.15, 0.15)
    c.drawString(MARGIN + 0.5 * inch, y, "Tips:")
    y -= 0.3 * inch

    tips = [
        "- Each student can color one piece before assembly.",
        "- Assemble on a large table or floor for best results.",
        f"- Final poster size: approx. {rows * 5.5:.0f}\" x {cols * 8.5:.0f}\".",
    ]

    c.setFont(BODY_FONT, 10)
    c.setFillColorRGB(0.35, 0.35, 0.35)
    for tip in tips:
        c.drawString(MARGIN + 0.6 * inch, y, tip)
        y -= 0.22 * inch

    # Footer
    c.setFont(SUBTITLE_FONT, 10)
    c.setFillColorRGB(0.6, 0.6, 0.6)
    c.drawCentredString(PAGE_WIDTH / 2, MARGIN + 0.3 * inch, title)

    c.showPage()
