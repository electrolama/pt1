# Design reference

This page distinguishes verified repository facts from operational assumptions. It
is intended as a fast pre-flight reference for modification and review.

## Source-of-truth order

When two descriptions differ, use this order:

1. checked-in KiCad source for the exact PCB revision;
2. physical inspection and measurement of that revision;
3. released manufacturing documentation for that revision, if added later;
4. generated pinout assets; and
5. prose documentation.

Report discrepancies rather than silently choosing the more convenient statement.

## Current revisions

| Domain | Current checked-in revision | Source |
| --- | --- | --- |
| Schematic and PCB | Rev A2 | `pcba/Rev A2/pt1-RevA2.kicad_*` |
| Enclosure | Rev A | `case/Rev A/*.stl` |
| Pinout presentation | unversioned | `pinout/` |

## External interfaces

| Interface | Data | Power | Notes |
| --- | --- | --- | --- |
| Upstream USB-C | USB 2.0 | input from host | connects the complete pt1 tool |
| Downstream USB-C | USB 2.0 | solder-jumper selected | switched or unswitched selection; never bridge both |
| Downstream USB-A | USB 2.0 | protected switched 5 V | follows DTR-controlled load switch |
| Six-pin header | USB 2.0 + UART | protected switched 5 V | also exposes ground |

## Header truth table

| Pin | Label | Electrical role |
| ---: | --- | --- |
| 1 | `VBUS_SW` | switched USB supply output |
| 2 | `RX_IN` | receive input to pt1 |
| 3 | `TX_OUT` | transmit output from pt1 |
| 4 | `USB_P3_N` | USB D− for hub port 3 |
| 5 | `USB_P3_P` | USB D+ for hub port 3 |
| 6 | `GND` | common ground |

## Control truth table

| Input or status | State | Meaning |
| --- | --- | --- |
| DTR | `False` / deasserted | switched power enabled |
| DTR | `True` / asserted | switched power disabled |
| RI | asserted | load-switch fault reported |
| PWR LED | lit | switched rail present at the indicator circuit |

## Repository does not currently include

- a released Gerber/drill fabrication archive;
- a released assembly BOM with manufacturer part numbers;
- a released pick-and-place/position file;
- PDF schematic or board-assembly drawings;
- automated KiCad ERC/DRC results; or
- measured compliance, signal-integrity, current-limit, or thermal test reports.

That absence is documented so source files are not mistaken for a verified
production pack. See [Build and manufacture](manufacturing.md) for the proposed
release process.

## Terminology

**Host**
: Computer or embedded Linux machine connected to pt1's upstream USB-C port.

**Target**
: Hardware being debugged, powered, or connected through pt1.

**Switched rail**
: Protected USB supply after the RT9742 load switch.

**Fault**
: Active load-switch report associated with over-current or over-temperature; it
  does not diagnose the underlying cause.

**DTR / RI**
: Traditional serial modem-control signals repurposed by pt1 for power control and
  fault reporting.

