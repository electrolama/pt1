# Repository guide

pt1 is a hardware-source repository rather than a firmware application. Its
structure should make three questions easy to answer: which revision is current,
where is the editable source, and which files are generated outputs?

## Layout

```text
pt1/
├── pcba/
│   └── Rev A2/                 editable KiCad project
├── case/
│   └── Rev A/                  printable STL outputs
├── pinout/                     original generator and artwork
├── documentation/
│   ├── assets/images/          all new and copied documentation imagery
│   ├── assets/stylesheets/     documentation-only presentation
│   ├── examples/               runnable usage examples
│   └── *.md                    task-oriented guides
├── .github/
│   ├── ISSUE_TEMPLATE/         structured reports
│   └── workflows/              strict docs build and Pages deployment
├── CONTRIBUTING.md
├── SUPPORT.md
├── mkdocs.yml
└── requirements-docs.txt
```

## Editable source versus output

| Area | Editable source | Generated or derived output |
| --- | --- | --- |
| PCB | `.kicad_sch`, `.kicad_pcb`, `.kicad_pro` | future Gerbers, drills, PDFs, BOM, positions |
| Pinout | `data.py`, `pinout_diagram.py`, `styles.css`, source board image | `diagram.svg` |
| Enclosure | not currently present | `.stl` meshes |
| Documentation | Markdown, CSS, examples, MkDocs config | `site/` (ignored) |
| Mascot art | prompt manifest | generated PNGs under `documentation/assets/images/` |

The missing editable case source is called out explicitly rather than implying the
STLs are convenient design inputs.

## Revision policy

- Create a new directory for a new physical revision.
- Keep older revisions available unless there is a safety or legal reason not to.
- Put revision identifiers on the physical design and in release notes.
- Never mix outputs from two hardware revisions in one fabrication pack.
- Document compatibility between PCB, enclosure, and any cable or fixture revision.

## Pinout regeneration

The checked-in script documents its own command:

```shell
cd pinout
python -m pinout.manager --export pinout_diagram.py diagram.svg
```

The generator depends on the third-party Python `pinout` package, but the current
repository does not pin that dependency. Until a tested version is recorded,
regeneration may differ from the checked-in SVG. A pinout change should update the
data/source and regenerated output together, then compare the rendered result.

## Documentation development

```shell
python -m venv .venv
# activate the environment for your shell
python -m pip install -r requirements-docs.txt
mkdocs serve
```

Before committing:

```shell
mkdocs build --strict
python -m compileall -q documentation/examples
```

The generated `site/` directory is ignored. Commit the Markdown, styles, and project
assets instead.

## Automation and publishing

`.github/workflows/documentation.yml` builds the site strictly and compiles the
Python examples on pull requests and pushes to the active hardware branches.

`.github/workflows/pages.yml` is intentionally manual until a maintainer enables
**Settings → Pages → Source: GitHub Actions** for the repository. After that one-time
setting, run **Publish documentation to GitHub Pages** from the Actions tab. Keeping
the first deployment manual avoids failing every branch build in repositories where
Pages has not yet been configured.

## Visual asset rule

Existing files under `pinout/` remain untouched. All artwork added by the 2026
documentation redesign—including copies used by the static-site build—lives under
`documentation/assets/images/`. Generation prompts and transparency checks are
recorded in [Visual asset provenance](assets/IMAGE_PROMPTS.md).
