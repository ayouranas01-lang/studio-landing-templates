# Collaborative Poster Generator

Convert any image into a TPT-ready (Teachers Pay Teachers) Collaborative Poster PDF product.

## Features

- **3 grid sizes**: 3×6 (18 pieces), 4×6 (24 pieces), 5×6 (30 pieces)
- **Complete PDF product** with Cover, Table of Contents, Assembly Guide, Poster Pieces, and Banner Pennants
- **Print-ready**: US Letter pages (8.5" × 11") with cutting lines and crop marks
- **Grid codes**: Each piece labeled (A1, A2, B1, B2, etc.) for easy assembly
- **Banner Pennants**: Triangular pennants with custom text for classroom decoration

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Generate a poster PDF
python main.py --input input/my_image.png --grid 4x6 --title "Back to School"
```

## Usage

```bash
python main.py [OPTIONS]

Options:
  -i, --input PATH       Source image (PNG/JPG) [required]
  -g, --grid TEXT         Grid size: 3x6, 4x6, or 5x6 [default: 4x6]
  -t, --title TEXT        Product title [default: Collaborative Poster]
  -s, --subtitle TEXT     Product subtitle
  -b, --banner-text TEXT  Text for banner pennants (defaults to title)
  -o, --output PATH      Output PDF path (auto-generated if omitted)
```

## Examples

```bash
# 3×6 grid
python main.py -i input/veterans_day.png -g 3x6 -t "Veterans Day"

# 4×6 grid with custom banner
python main.py -i input/earth_day.png -g 4x6 -t "Earth Day" -b "EARTH DAY"

# 5×6 grid with custom output path
python main.py -i input/spring.png -g 5x6 -t "Spring" -o output/spring_poster.pdf
```

## Output Structure

The generated PDF contains these pages in order:

1. **Cover Page** — Product title, thumbnail preview, and specifications
2. **Table of Contents** — Indexed list of all sections
3. **Assembly Guide** — Grid map with codes + step-by-step instructions
4. **Poster Pieces** — One page per piece with cutting lines and grid code
5. **Banner Pennants** — Triangular pennants for classroom decoration

## Grid Code System

Each piece is labeled with a row letter + column number:

|     | Col 1 | Col 2 | Col 3 | Col 4 | Col 5 | Col 6 |
|-----|-------|-------|-------|-------|-------|-------|
| Row A | A1 | A2 | A3 | A4 | A5 | A6 |
| Row B | B1 | B2 | B3 | B4 | B5 | B6 |
| Row C | C1 | C2 | C3 | C4 | C5 | C6 |
| ... | ... | ... | ... | ... | ... | ... |

## Requirements

- Python 3.10+
- Pillow >= 10.0
- ReportLab >= 4.0
- Click >= 8.0
