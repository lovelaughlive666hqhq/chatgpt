#!/usr/bin/env python3
"""OCR scanner to extract text from image files into editable text files."""

from __future__ import annotations

import argparse
from pathlib import Path
from typing import Iterable

SUPPORTED_EXTENSIONS = {".png", ".jpg", ".jpeg", ".tif", ".tiff", ".bmp", ".webp"}


def iter_images(path: Path, recursive: bool = True) -> Iterable[Path]:
    if path.is_file():
        if path.suffix.lower() in SUPPORTED_EXTENSIONS:
            yield path
        return

    globber = path.rglob if recursive else path.glob
    for file_path in globber("*"):
        if file_path.is_file() and file_path.suffix.lower() in SUPPORTED_EXTENSIONS:
            yield file_path


def ocr_image(image_path: Path, language: str = "eng") -> str:
    from PIL import Image
    import pytesseract

    with Image.open(image_path) as image:
        return pytesseract.image_to_string(image, lang=language)


def write_text_output(text: str, source_path: Path, output_dir: Path) -> Path:
    output_dir.mkdir(parents=True, exist_ok=True)
    output_file = output_dir / f"{source_path.stem}.txt"
    output_file.write_text(text, encoding="utf-8")
    return output_file


def main() -> int:
    parser = argparse.ArgumentParser(
        description=(
            "Extract text from image files and save as editable .txt files. "
            "Input can be a single image file or a directory."
        )
    )
    parser.add_argument("input", type=Path, help="Image file or directory containing image files")
    parser.add_argument(
        "-o",
        "--output-dir",
        type=Path,
        default=Path("ocr_output"),
        help="Directory where extracted text files are written (default: ./ocr_output)",
    )
    parser.add_argument(
        "-l",
        "--language",
        default="eng",
        help="Tesseract OCR language code (default: eng)",
    )
    parser.add_argument(
        "--non-recursive",
        action="store_true",
        help="When input is a directory, scan only top-level files",
    )

    args = parser.parse_args()

    if not args.input.exists():
        print(f"Input path not found: {args.input}")
        return 1

    images = list(iter_images(args.input, recursive=not args.non_recursive))
    if not images:
        print("No supported image files found.")
        return 1

    try:
        import PIL  # noqa: F401
        import pytesseract  # noqa: F401
    except ModuleNotFoundError as error:
        print(
            "Missing dependency. Install required packages with: "
            "pip install -r requirements.txt"
        )
        print(f"Details: {error}")
        return 1

    success_count = 0
    failure_count = 0

    for image_path in images:
        try:
            text = ocr_image(image_path, language=args.language)
            output_path = write_text_output(text, image_path, args.output_dir)
            print(f"Processed {image_path} -> {output_path}")
            success_count += 1
        except Exception as error:
            print(f"Failed to process {image_path}: {error}")
            failure_count += 1

    print(
        f"Completed OCR. Success: {success_count}, Failed: {failure_count}, "
        f"Total: {len(images)}"
    )
    return 0 if success_count > 0 and failure_count == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
