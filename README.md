# OCR Scanner

A simple OCR scanner that extracts text from image files and writes editable `.txt` outputs.

## Features
- Supports single-image input or whole-folder scanning
- Recursively scans folders by default
- Outputs one text file per image
- Uses Tesseract OCR engine via `pytesseract`

## Supported image formats
`.png`, `.jpg`, `.jpeg`, `.tif`, `.tiff`, `.bmp`, `.webp`

## Setup
1. Install system dependency: **Tesseract OCR**
2. Install Python dependencies:

```bash
pip install -r requirements.txt
```

## Usage

```bash
python ocr_scanner.py <input_file_or_directory> -o <output_dir>
```

Examples:

```bash
# Scan one file
python ocr_scanner.py ./images/page1.png

# Scan a folder recursively
python ocr_scanner.py ./images -o ./extracted_text

# Use another language model (if installed in Tesseract)
python ocr_scanner.py ./images -l eng
```

Output text files are written as `<image_name>.txt` in the output directory.
