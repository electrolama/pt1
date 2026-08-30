# Documentation research

The 2026 repository redesign reviewed several projects whose documentation handles
complex hardware particularly well. The goal was not to imitate their branding,
but to extract repeatable structural patterns.

## Projects reviewed

### Bus Pirate

The [Bus Pirate hardware documentation](https://docs.buspirate.com/docs/overview/hardware/)
separates user concepts, detailed hardware design, components, enclosures,
manufacturing, development, and revision-specific material. Individual interface
pages pair exact pin tables with operational context, while the manufacturing area
makes physical production a first-class documentation topic.

**Applied to pt1:** task-based navigation, a conceptual architecture before
net-level detail, explicit power/fault semantics, enclosure guidance, manufacturing
checks, and strong cross-links between use and design.

### SparkFun GNSS Flex System

The [SparkFun GNSS Flex repository](https://github.com/sparkfun/SparkFun_GNSS_Flex_System)
publishes a clear repository-content map and groups each board's design files,
schematic, dimensions, 3D models, component documentation, and hookup-guide images
in predictable locations.

**Applied to pt1:** a repository map, explicit source/output distinction, dedicated
documentation assets, and a proposed release-pack layout.

### HackRF

The [HackRF repository](https://github.com/greatscottgadgets/hackrf) keeps raw docs
with the code, explains how to build them, accepts documentation pull requests, and
has separate sections for hardware platforms, revisions, components, connectors,
enclosures, troubleshooting, and development. Its
[hardware-revision guide](https://github.com/greatscottgadgets/hackrf/blob/main/docs/source/list_of_hardware_revisions.rst)
preserves the history and explains how to identify revisions physically.

**Applied to pt1:** docs-as-source, strict local builds, a revision policy, clear
support boundaries, and revision-specific contributor evidence.

### Adafruit Learning System

Adafruit's [guide to PCB design files](https://learn.adafruit.com/accessing-and-using-adafruit-pcb-design-files)
bridges the gap between publishing CAD files and helping someone find, download,
open, and use them. Product guides consistently expose downloads and fabrication
references alongside practical learning material.

**Applied to pt1:** direct paths to editable files, explanations of file roles, and
warnings where a source or release artifact is absent.

### Zephyr board documentation

Zephyr's [board documentation guidance](https://docs.zephyrproject.org/latest/contribute/documentation/guidelines.html)
uses consistent board-page structure and generated supported-hardware data, while
its [board porting guide](https://docs.zephyrproject.org/latest/hardware/porting/board_porting.html)
defines a predictable hierarchy for hardware support.

**Applied to pt1:** a stable information template—identity, supported interfaces,
setup, source location, limitations, and contribution path—and a bias toward facts
that can ultimately be generated or checked from source.

## Resulting principles

1. **Orient first.** State the tool's job in one sentence and show its topology.
2. **Separate tasks from internals.** Users should not read a schematic to connect a
   UART, while modifiers still need a net-level source of truth.
3. **Treat power as a safety surface.** Polarity, startup behavior, faults, and
   back-powering belong in the main path.
4. **Name revisions everywhere they matter.** PCB and enclosure compatibility must
   not be inferred from filenames alone.
5. **Do not confuse editable source with a production release.** A fabrication pack
   needs generation metadata, independent visual review, checks, and prototype
   evidence.
6. **Keep documentation reproducible.** Build instructions, strict CI, relative
   links, asset provenance, and runnable examples make maintenance realistic.
7. **Add character without hiding information.** Mascots support wayfinding and
   tone; diagrams, tables, warnings, and source paths carry the technical truth.

