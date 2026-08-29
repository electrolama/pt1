# Build and manufacture

The repository currently provides editable KiCad Rev A2 source and printable Rev A
STLs. It does **not** yet provide a reviewed, versioned fabrication release. This
guide defines what a trustworthy release should contain.

## Open the design

Use a KiCad version compatible with the checked-in file format and open:

```text
pcba/Rev A2/pt1-RevA2.kicad_pro
```

Before changing anything, confirm that symbols, footprints, fonts, and 3D models
resolve without substitution. Do not save the design merely to dismiss a version
warning; review the resulting diff first.

## Pre-fabrication review

### Schematic

- Run ERC and classify every exclusion.
- Verify USB-C CC configuration and connector roles.
- Verify DTR-to-enable and fault-to-RI polarity.
- Check load-switch timing, current-limit behavior, thermal limits, and absolute
  maximum ratings against current datasheets.
- Review every power path and possible back-power route.
- Confirm TVS parts, return paths, and connector placement.

### PCB

- Run DRC using the intended manufacturer's minimum capabilities.
- Confirm board outline, slots, holes, and connector edge clearances.
- Review USB 2.0 differential routing against the actual layer stack-up.
- Inspect return paths and discontinuities around protection devices and vias.
- Check copper-to-edge, solder-mask dams, silkscreen, paste apertures, and courtyard
  collisions.
- Verify polarity, pin 1, connector gender, and assembly-side orientation.

### Mechanical

- Compare board geometry with the selected Rev A enclosure.
- Test actual plugs, not only nominal connector bodies.
- Confirm the header-population choice matches the top shell.
- Check mounting hardware for component and copper clearance.

## Proposed release pack

A future release directory should be immutable and named for the hardware revision,
for example `releases/Rev-A2/`. It should include:

```text
Rev-A2/
├── README.md                 generation date, commit, tools, and checksums
├── schematic.pdf
├── assembly-drawing-top.pdf
├── assembly-drawing-bottom.pdf
├── bom.csv                   validated values, packages, and MPNs
├── positions.csv             reviewed units, origin, rotation, and side
├── gerbers/                  copper, mask, silk, and outline
├── drills/                   plated and non-plated drill outputs
├── ipc356/                   optional electrical netlist
└── checks/                   ERC, DRC, visual-review, and test records
```

Do not call a pack production-ready solely because the EDA tool exported it.

## Release validation

1. Generate from a clean checkout at a named commit.
2. Record KiCad and plugin versions.
3. Open every Gerber and drill file in an independent viewer.
4. Compare the plotted stack against the PCB source layer by layer.
5. Cross-check BOM quantities against placed references.
6. Review position-file origin, units, rotations, and board side with the assembler.
7. Validate connector overhangs, mounting holes, and outline dimensions.
8. Archive ERC/DRC output and explain approved exceptions.
9. Build and test prototypes before promoting the pack to a release.

## Bring-up checklist

- Inspect for shorts, reversed parts, bridges, and connector damage.
- Check resistance between USB supply and ground before connection.
- First-power through an appropriate current-limited setup.
- Verify unswitched rails before enabling switched power.
- Confirm hub and serial enumeration.
- Confirm DTR polarity, startup delay, RI fault behavior, and PWR LED.
- Exercise each downstream USB data path.
- Test switched output under representative load and inrush.
- Check thermal behavior and recovery.
- Record the PCB revision and test setup with results.

!!! danger "Compliance and USB interoperability"
    Open source files do not confer regulatory approval or USB compliance. Anyone
    manufacturing or selling hardware is responsible for applicable electrical
    safety, EMC, materials, labelling, USB, and local-market requirements.

