#!/usr/bin/env python3
"""CLI entry point for Collaborative Poster Generator."""

import sys
from pathlib import Path

import click

from poster_generator.pdf_compiler import compile_pdf


@click.command()
@click.option(
    "--input", "-i",
    "input_path",
    required=True,
    type=click.Path(exists=True, path_type=Path),
    help="Path to the source image (PNG/JPG).",
)
@click.option(
    "--grid", "-g",
    default="4x6",
    show_default=True,
    help="Grid size: 3x6, 4x6, or 5x6.",
)
@click.option(
    "--title", "-t",
    default="Collaborative Poster",
    show_default=True,
    help="Product title.",
)
@click.option(
    "--subtitle", "-s",
    default="Collaborative Coloring Activity",
    show_default=True,
    help="Product subtitle.",
)
@click.option(
    "--banner-text", "-b",
    default=None,
    help="Text for banner pennants (defaults to title).",
)
@click.option(
    "--output", "-o",
    "output_path",
    default=None,
    type=click.Path(path_type=Path),
    help="Output PDF path (auto-generated if omitted).",
)
def main(
    input_path: Path,
    grid: str,
    title: str,
    subtitle: str,
    banner_text: str | None,
    output_path: Path | None,
) -> None:
    """Convert an image into a TPT-ready Collaborative Poster PDF.

    Supports grid sizes: 3x6, 4x6, 5x6.

    Example usage:

        python main.py -i input/poster.png -g 4x6 -t "Back to School"
    """
    # Validate grid
    valid_grids = {"3x6", "4x6", "5x6"}
    if grid.lower() not in valid_grids:
        click.echo(f"Error: Grid must be one of {valid_grids}. Got '{grid}'.", err=True)
        sys.exit(1)

    # Auto-generate output path if not provided
    if output_path is None:
        stem = input_path.stem
        output_path = Path("output") / f"{stem}_{grid}_poster.pdf"

    click.echo(f"Input image : {input_path}")
    click.echo(f"Grid size   : {grid}")
    click.echo(f"Title       : {title}")
    click.echo(f"Output      : {output_path}")
    click.echo()

    result = compile_pdf(
        image_path=input_path,
        output_path=output_path,
        grid=grid,
        title=title,
        subtitle=subtitle,
        banner_text=banner_text,
    )

    click.echo(f"PDF generated successfully: {result}")


if __name__ == "__main__":
    main()
