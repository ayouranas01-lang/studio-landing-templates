"""Compile all pages into a single PDF file."""

from pathlib import Path

from PIL import Image
from reportlab.pdfgen.canvas import Canvas

from .assembly_guide import draw_assembly_guide
from .banner_pennants import draw_banner_pennants
from .cover_page import draw_cover_page
from .page_builder import draw_piece_page
from .splitter import split_image
from .toc_builder import draw_toc_page
from .utils import PAGE_HEIGHT, PAGE_WIDTH, parse_grid


def compile_pdf(
    image_path: str | Path,
    output_path: str | Path,
    grid: str = "4x6",
    title: str = "Collaborative Poster",
    subtitle: str = "Collaborative Coloring Activity",
    banner_text: str | None = None,
) -> Path:
    """Build the complete product PDF.

    Parameters
    ----------
    image_path : path to the source image.
    output_path : path for the generated PDF.
    grid : grid size string, e.g. '3x6', '4x6', '5x6'.
    title : product title shown on cover and headers.
    subtitle : product subtitle shown on cover.
    banner_text : optional text for the banner pennants (defaults to *title*).

    Returns
    -------
    Path to the written PDF file.
    """
    rows, cols = parse_grid(grid)
    image_path = Path(image_path)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)

    full_image = Image.open(image_path).convert("RGBA")

    # Split the image
    pieces = split_image(image_path, rows, cols)

    # Create the PDF canvas
    c = Canvas(str(output_path), pagesize=(PAGE_WIDTH, PAGE_HEIGHT))
    c.setTitle(title)
    c.setAuthor("Collaborative Poster Generator")

    # 1. Cover page
    draw_cover_page(c, title, subtitle, rows, cols, full_image)

    # 2. Table of Contents
    draw_toc_page(c, title, rows, cols)

    # 3. Assembly Guide
    draw_assembly_guide(c, title, rows, cols, full_image)

    # 4. Poster pieces
    for piece in pieces:
        draw_piece_page(c, piece["image"], piece["code"])

    # 5. Banner Pennants
    draw_banner_pennants(c, title, banner_text, full_image)

    c.save()
    return output_path
