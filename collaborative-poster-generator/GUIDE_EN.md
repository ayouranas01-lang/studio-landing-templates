# Collaborative Poster Generator — User Guide

## Overview

A Python tool that converts any image into a TPT-ready (Teachers Pay Teachers) Collaborative Poster PDF product.

The tool generates two versions:
- **Color version** — The original image split into grid pieces
- **Black & White version** — Outline-only coloring pages for students

---

## 1. Install Requirements

Make sure Python 3.10+ is installed, then run:

```bash
pip install -r requirements.txt
```

---

## 2. Prepare Your Images

Place your image (PNG or JPG) in the `input/` folder:

```
collaborative-poster-generator/
├── input/
│   ├── your_image.png      ← Place your image here
│   └── another_image.jpg
```

**Image recommendations:**
- Minimum recommended: 1800×1200 pixels (for print quality)
- Supported formats: PNG, JPG, JPEG
- Landscape orientation works best

---

## 3. Run the Tool

### Generate both versions (Color + Black & White)

```bash
cd collaborative-poster-generator
python main.py -i input/your_image.png -g 4x6 -t "Back to School" -m both --zip
```

### Generate color version only

```bash
python main.py -i input/your_image.png -g 4x6 -t "Back to School" -m color
```

### Generate black & white version only

```bash
python main.py -i input/your_image.png -g 4x6 -t "Back to School" -m bw
```

---

## 4. Command Options

| Option | Short | Description | Default |
|--------|-------|-------------|---------|
| `--input` | `-i` | Input image path (required) | — |
| `--grid` | `-g` | Grid size: `3x6`, `4x6`, or `5x6` | `4x6` |
| `--title` | `-t` | Product title | `Collaborative Poster` |
| `--subtitle` | `-s` | Product subtitle | `Collaborative Coloring Activity` |
| `--banner-text` | `-b` | Text for pennant banners (defaults to title) | — |
| `--mode` | `-m` | Output mode: `color`, `bw`, or `both` | `both` |
| `--output` | `-o` | Custom PDF output path | auto-generated |
| `--zip` | — | Package all output files into a ZIP archive | off |

---

## 5. Grid Sizes

| Size | Rows × Columns | Total Pieces |
|------|-----------------|--------------|
| `3x6` | 3 × 6 | 18 pieces |
| `4x6` | 4 × 6 | 24 pieces |
| `5x6` | 5 × 6 | 30 pieces |

---

## 6. Output Files

After running the command, find your files in the `output/` folder:

```
output/
└── your_image_4x6/
    ├── your_image_4x6_color.pdf      ← Full-color version
    ├── your_image_4x6_bw.pdf         ← Black & white coloring version
    └── your_image_4x6_product.zip    ← ZIP archive (if --zip was used)
```

### Each PDF contains:

1. **Cover Page** — Product title with thumbnail preview
2. **Table of Contents** — Indexed page listing
3. **Assembly Guide** — Grid map with codes + step-by-step instructions
4. **Poster Pieces** — Each piece on a US Letter page with cutting lines and grid code (A1, B2, etc.)
5. **Banner Pennants** — Triangular cut-out letters for classroom decoration

---

## 7. Full Example

```bash
# 1. Place your image in the input folder
cp ~/Downloads/earth_day_poster.png input/

# 2. Run the tool (both versions + ZIP)
python main.py -i input/earth_day_poster.png -g 4x6 -t "Earth Day" -b "EARTH DAY" -m both --zip

# 3. Output files:
#    output/earth_day_poster_4x6/earth_day_poster_4x6_color.pdf
#    output/earth_day_poster_4x6/earth_day_poster_4x6_bw.pdf
#    output/earth_day_poster_4x6/earth_day_poster_4x6_product.zip
```

---

## 8. Upload to TPT

1. Upload the ZIP file to your TPT store
2. Or upload both PDF files separately (color + coloring version)
3. Use the cover page as the product preview image

---

## 9. Troubleshooting

| Problem | Solution |
|---------|----------|
| `No such file or directory` | Make sure the image exists in the `input/` folder |
| `Grid must be one of` | Use one of: `3x6`, `4x6`, `5x6` |
| Low print quality | Use an image at least 1800×1200 pixels |
