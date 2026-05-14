"""Split an input image into a grid of segments."""

from pathlib import Path

from PIL import Image, ImageFilter, ImageOps

from .utils import ROW_LABELS, grid_code


def _to_coloring_page(img: Image.Image) -> Image.Image:
    """Convert a color image into a black-and-white coloring-page outline."""
    gray = img.convert("L")
    edges = gray.filter(ImageFilter.FIND_EDGES)
    inverted = ImageOps.invert(edges)
    threshold = inverted.point(lambda p: 255 if p > 200 else 0)
    return threshold.convert("RGBA")


def split_image(
    image_path: str | Path,
    rows: int,
    cols: int,
    output_dir: str | Path | None = None,
    bw: bool = False,
) -> list[dict]:
    """Split *image_path* into a rows×cols grid and return metadata for each piece.

    Each piece is cropped from the source image.  If *output_dir* is given the
    pieces are also saved to disk as PNG files.

    Parameters
    ----------
    bw : If True, convert each piece to a black-and-white coloring outline.

    Returns a list of dicts::

        [{"code": "A1", "row": 0, "col": 0, "image": <PIL.Image>}, ...]
    """
    img = Image.open(image_path).convert("RGBA")
    img_w, img_h = img.size

    piece_w = img_w // cols
    piece_h = img_h // rows

    if output_dir is not None:
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

    pieces: list[dict] = []

    for r in range(rows):
        for c in range(cols):
            left = c * piece_w
            upper = r * piece_h
            right = left + piece_w if c < cols - 1 else img_w
            lower = upper + piece_h if r < rows - 1 else img_h

            piece_img = img.crop((left, upper, right, lower))

            if bw:
                piece_img = _to_coloring_page(piece_img)

            code = grid_code(r, c)

            if output_dir is not None:
                piece_img.save(output_dir / f"{code}.png")

            pieces.append(
                {
                    "code": code,
                    "row": r,
                    "col": c,
                    "image": piece_img,
                }
            )

    return pieces
