# Collaborative Poster Generator

Convert any image into a TPT-ready (Teachers Pay Teachers) Collaborative Poster PDF product.

**📖 Guides:** [English Guide](GUIDE_EN.md) | [الدليل بالعربية](GUIDE_AR.md)

## Features

- **3 grid sizes**: 3×6 (18 pieces), 4×6 (24 pieces), 5×6 (30 pieces)
- **2 output modes**: Full-color version + Black & White coloring version
- **Complete PDF product** with Cover, Table of Contents, Assembly Guide, Poster Pieces, and Banner Pennants
- **Print-ready**: US Letter pages (8.5" × 11") with cutting lines and crop marks
- **Grid codes**: Each piece labeled (A1, A2, B1, B2, etc.) for easy assembly
- **ZIP packaging**: Bundle all files into a single archive for upload to TPT

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt

# Generate both color + B&W versions with ZIP
python main.py -i input/my_image.png -g 4x6 -t "Back to School" -m both --zip
```

## Usage

```bash
python main.py [OPTIONS]

Options:
  -i, --input PATH          Source image (PNG/JPG) [required]
  -g, --grid TEXT            Grid size: 3x6, 4x6, or 5x6 [default: 4x6]
  -t, --title TEXT           Product title [default: Collaborative Poster]
  -s, --subtitle TEXT        Product subtitle
  -b, --banner-text TEXT     Text for banner pennants (defaults to title)
  -m, --mode [color|bw|both] Output mode [default: both]
  -o, --output PATH          Custom output PDF path
  --zip                      Package output files into a ZIP archive
```

## Output Structure

```
output/
└── my_image_4x6/
    ├── my_image_4x6_color.pdf     # Full-color version
    ├── my_image_4x6_bw.pdf        # Black & white coloring version
    └── my_image_4x6_product.zip   # ZIP archive (with --zip flag)
```

## Requirements

- Python 3.10+
- Pillow >= 10.0
- ReportLab >= 4.0
- Click >= 8.0
