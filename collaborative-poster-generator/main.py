#!/usr/bin/env python3
"""CLI entry point for Collaborative Poster Generator."""

import sys
import zipfile
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
@click.option(
    "--mode", "-m",
    type=click.Choice(["color", "bw", "both"], case_sensitive=False),
    default="both",
    show_default=True,
    help="Output mode: color, bw (black & white), or both.",
)
@click.option(
    "--zip", "create_zip",
    is_flag=True,
    default=False,
    help="Package all output files into a ZIP archive.",
)
def main(
    input_path: Path,
    grid: str,
    title: str,
    subtitle: str,
    banner_text: str | None,
    output_path: Path | None,
    mode: str,
    create_zip: bool,
) -> None:
    """Convert an image into a TPT-ready Collaborative Poster PDF.

    Supports grid sizes: 3x6, 4x6, 5x6.
    Generates color version, black & white coloring version, or both.

    Example usage:

    \b
        python main.py -i input/poster.png -g 4x6 -t "Back to School"
        python main.py -i input/poster.png -g 4x6 -t "Earth Day" -m both --zip
    """
    valid_grids = {"3x6", "4x6", "5x6"}
    if grid.lower() not in valid_grids:
        click.echo(f"Error: Grid must be one of {valid_grids}. Got '{grid}'.", err=True)
        sys.exit(1)

    stem = input_path.stem
    output_dir = Path("output") / f"{stem}_{grid}"
    output_dir.mkdir(parents=True, exist_ok=True)

    click.echo(f"Input image : {input_path}")
    click.echo(f"Grid size   : {grid}")
    click.echo(f"Title       : {title}")
    click.echo(f"Mode        : {mode}")
    click.echo()

    generated_files: list[Path] = []

    if mode in ("color", "both"):
        color_path = output_path or (output_dir / f"{stem}_{grid}_color.pdf")
        click.echo("Generating COLOR version...")
        result = compile_pdf(
            image_path=input_path,
            output_path=color_path,
            grid=grid,
            title=title,
            subtitle=subtitle,
            banner_text=banner_text,
            bw=False,
        )
        click.echo(f"  -> {result}")
        generated_files.append(result)

    if mode in ("bw", "both"):
        bw_path = output_dir / f"{stem}_{grid}_bw.pdf"
        click.echo("Generating BLACK & WHITE version...")
        result = compile_pdf(
            image_path=input_path,
            output_path=bw_path,
            grid=grid,
            title=title,
            subtitle=subtitle,
            banner_text=banner_text,
            bw=True,
        )
        click.echo(f"  -> {result}")
        generated_files.append(result)

    if create_zip and generated_files:
        zip_path = output_dir / f"{stem}_{grid}_product.zip"
        with zipfile.ZipFile(zip_path, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in generated_files:
                zf.write(f, f.name)
        click.echo(f"\nZIP archive : {zip_path}")

    click.echo("\nDone!")


if __name__ == "__main__":
    main()
