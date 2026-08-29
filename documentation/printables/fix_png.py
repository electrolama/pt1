"""Rewrite PNG files as clean RGB/RGBA images for reliable SVG embedding."""

from pathlib import Path
from sys import argv

from PIL import Image


def clean_png(path: Path) -> None:
    try:
        with Image.open(path) as image:
            cleaned = image.convert("RGBA" if image.mode in ("RGBA", "LA", "P") else "RGB")
            temporary = path.with_suffix(".tmp.png")
            cleaned.save(temporary, format="PNG", optimize=False, compress_level=6)
            temporary.replace(path)
        print(f"[OK] {path}")
    except Exception as error:
        print(f"[FAIL] {path} -> {error}")


def main() -> None:
    root = Path(argv[1]) if len(argv) > 1 else Path(".")
    png_files = list(root.rglob("*.png"))
    print(f"Found {len(png_files)} PNG files")
    for png in png_files:
        clean_png(png)
    print("Done")


if __name__ == "__main__":
    main()
