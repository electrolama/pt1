# Contributing to pt1

Thank you for helping improve pt1. Hardware changes have physical consequences, so
good contributions make the intent, revision scope, and validation evidence clear.

## Before opening a pull request

1. Open or reference an issue for changes that affect interfaces, protection,
   power routing, PCB geometry, connectors, or enclosure fit.
2. State which revision you tested. The current checked-in sources are PCB Rev A2
   and case Rev A.
3. Keep generated documentation images inside `documentation/assets/images/`.
   Do not replace or modify the original files in `pinout/` unless the change is
   specifically about the pinout source pipeline.
4. Do not commit fabrication outputs as though they are release-ready unless they
   were generated from a clean source checkout and independently reviewed.
5. Build the documentation with `mkdocs build --strict`.

## Change-specific evidence

| Change | Include with the pull request |
| --- | --- |
| Schematic | Annotated PDF or screenshots, ERC result, and rationale |
| PCB layout | DRC result, changed-layer screenshots, and clearance/stack-up assumptions |
| USB data path | Routing/impedance assumptions and test evidence appropriate to USB 2.0 |
| Power path | Load, inrush, fault, thermal, and recovery observations |
| Enclosure | Slicer preview, print settings, photographs, and fit notes |
| Documentation | Screenshots for visual changes and confirmation that strict build passes |

## Repository conventions

- Put each hardware revision in its own directory; do not silently overwrite an
  earlier revision.
- Use descriptive commits and keep source changes separate from generated outputs
  where practical.
- Prefer relative links in Markdown.
- Explain whether a statement was measured, calculated, taken from a datasheet, or
  inferred from the design.
- Keep examples safe by default: target power off on exit, explicit DTR state, and
  fault handling where relevant.

See the full [contributor guide](documentation/contributing.md) for the review
workflow and release checklist.

