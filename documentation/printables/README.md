# pt1 printables

`pt1-postcard-6x4.svg` is the editable, self-contained light-mode source. It uses
a 1800 × 1200 view box and declares a physical size of exactly 6 × 4 inches. The
generated PDF uses the same finished size.

The QR code links to:

```text
https://lab.electrolama.com/project/pt1
```

## Rebuild

Install the QR dependency in an isolated Python environment, then run:

```shell
python -m pip install "qrcode[pil]>=8,<9"
python documentation/printables/fix_png.py documentation/assets/images
python documentation/printables/build_postcard.py
inkscape documentation/printables/pt1-postcard-6x4.svg \
  --export-filename=documentation/printables/pt1-postcard-6x4.pdf
```

The postcard embeds its raster artwork as data URIs, so the final SVG does not
depend on external image paths. The QR geometry and all typography/layout shapes
remain vector content.

`fix_png.py` strips PNG metadata and rewrites the generated artwork as ordinary
RGB/RGBA PNGs before embedding. This avoids Inkscape's broken-image placeholder
when it encounters some AI-generated PNG encodings.
