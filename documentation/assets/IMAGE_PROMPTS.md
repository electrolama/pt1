# Visual asset provenance

All new illustrations were generated on 2026-08-29 with Codex's built-in image
generation tool. Existing files under `pinout/` were not edited. The documentation
copies `board-source.png` and `pinout-source.svg` are byte-for-byte copies of the
original `pinout/board.png` and `pinout/diagram.svg`, placed here so the static site
can build without reaching outside its documentation root.

## Art direction

- audience: experienced makers;
- tone: technically competent, playful, and clean rather than childish;
- palette: charcoal PCB black, warm cream, electric yellow, with restrained cyan
  and magenta signal accents;
- mascot: an original chibi llama electronics engineer with safety glasses and a
  dark maker apron; and
- constraints: no brand marks, captions, watermarks, or copied board artwork.

## Generated assets

| File | Intended use | Transparency verified |
| --- | --- | --- |
| `images/pt1-hero.png` | README and documentation landing hero | opaque by design |
| `images/llama-power.png` | power-control guidance | yes, alpha 0–255 |
| `images/llama-protection.png` | protection and fault callouts | yes, alpha 0–255 |
| `images/llama-build.png` | assembly and enclosure guidance | yes, alpha 0–255 |
| `images/llama-uart.png` | serial and troubleshooting guidance | yes, alpha 0–255 |
| `images/llama-frame.png` | optional frame around technical diagrams | yes, alpha 0–255 |

## Final prompt set

### Hero

> Create a polished wide documentation banner for an open-source electronics
> debugging tool: one original tiny chibi llama electronics engineer beside a
> generic compact black USB debugging PCB, with energetic lightning bolts. Use a
> clean deep-charcoal laboratory backdrop, subtle circuit traces, crisp premium 2D
> editorial illustration, vector-like edges, and screen-print texture. The llama
> wears a maker apron and safety glasses and holds a multimeter probe. Use charcoal,
> warm cream, electric yellow, and small cyan/magenta accents. No text, logos,
> watermark, copied board artwork, clutter, or dangerous arcing.

### Power

> Create a transparent compact spot illustration of the same chibi llama engineer
> operating a large safe toggle switch, with two electric-yellow lightning bolts
> indicating USB power cycling. Preserve the cream fleece, safety glasses, dark
> apron, crisp editorial/vector-like style, screen-print texture, and restrained
> cyan/magenta accents. Exactly one llama; no text, logos, border, watermark,
> clutter, or dangerous arcing.

### Protection

> Create a transparent compact spot illustration of the same chibi llama engineer
> kneeling beside a tiny protected USB board and calmly holding a shield that catches
> one yellow lightning bolt, symbolising over-current protection and fault reporting.
> Keep the established character and palette. Exactly one llama; no text, logos,
> border, watermark, fire, smoke, panic, or clutter.

### Build

> Create a transparent compact spot illustration of the same chibi llama engineer
> assembling a tiny black PCB at a tidy ESD-safe workbench, holding a fine soldering
> iron correctly, with two small yellow lightning motifs. Keep the established
> character, palette, vector-like editorial style, and screen-print texture. Exactly
> one llama; no text, logos, border, watermark, smoke, clutter, or unsafe soldering.

### UART

> Create a transparent compact spot illustration of one chibi llama electronics
> engineer tracing UART signals between a laptop terminal and a small target board,
> using a magnifying glass over neat cyan and magenta TX/RX signal lines and one
> yellow lightning accent. Keep the established character and palette. Show three
> tidy jumper wires. No text, logos, border, watermark, tangled wires, clutter, or
> extra characters.

### Frame

> Create a transparent 16:9 documentation frame made from thin elegant black PCB
> traces and electric-yellow lightning details, with four very small chibi llama
> engineer heads peeking from the corners. Keep the entire centre empty and
> transparent. Use charcoal, warm cream, yellow, and tiny cyan/magenta accents. No
> text, logos, watermark, filled backdrop, thick ornament, or objects intruding into
> the centre.

## Extraction pass

The initial power, UART, and frame images rendered a visible checkerboard rather
than an alpha channel. Each was passed back through background extraction with the
instruction to change only the checkerboard to genuine transparency and preserve
the illustration, fine edges, colours, proportions, and composition. The final PNG
alpha ranges were verified programmatically.

