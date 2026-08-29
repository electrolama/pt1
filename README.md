# pt1

![pt1 — a compact USB bring-up and debugging multitool](documentation/assets/images/pt1-hero.png)

**One cable in. A hub, UART, and controllable target power out.**

pt1 is an open-hardware USB multitool for experienced makers doing board bring-up,
firmware development, and field diagnostics. Its approximately 46 × 18 mm PCB
combines:

- a four-port USB 2.0 hub, with one port used by the onboard serial bridge;
- USB-C and USB-A downstream connections;
- a CH343P USB-to-UART interface;
- a protected, software-switchable 5 V rail with fault reporting; and
- a six-pin header exposing UART, USB 2.0, switched power, and ground.

The useful trick is that the serial adapter's modem-control signals do double duty:
**DTR controls target power** and **RI reports an over-current or over-temperature
fault**. That lets a test rig open a console, cycle a target, and detect a power
problem through the same USB connection.

> [!CAUTION]
> pt1 is a USB debugging tool, not a calibrated power meter. Confirm the target's
> voltage and current requirements before connecting it, and do not bridge both
> sides of the downstream USB-C power-selection solder jumper.

## Start here

1. Connect the host to pt1's upstream USB-C port.
2. Wait for the USB hub and CH343 serial port to enumerate.
3. For a UART target, connect target TX → `RX_IN`, target RX → `TX_OUT`, and ground
   → `GND`.
4. Use [Vicuña's pt1 mode](https://lab.electrolama.com/project/vicuna) for an
   integrated terminal, power toggle, and fault indicator—or use the
   [Python example](documentation/examples/power_cycle.py).
5. Read the [getting-started guide](documentation/getting-started.md) before using
   switched power.

## Hardware at a glance

| Function | Implementation | What it gives you |
| --- | --- | --- |
| USB expansion | SL2.1A four-port USB 2.0 hub | Two sockets, one header port, and the internal serial bridge |
| Serial | CH343P USB-to-UART bridge | Target console plus DTR/RI control signals |
| Protected power | RT9742CGJ5 load switch | Current limiting, thermal protection, and active-low fault output |
| Data-line protection | TVS arrays | Transient protection on USB data pairs |
| Mechanical | Three 2 mm mounting holes and printable case | Bench-friendly mounting and enclosure options |

![pt1 pinout](documentation/assets/images/pinout-source.svg)

## Documentation

| I want to… | Go to… |
| --- | --- |
| Connect a board safely | [Getting started](documentation/getting-started.md) |
| Identify a connector or header pin | [Pinout and connections](documentation/pinout.md) |
| Automate power cycling and fault detection | [Power control](documentation/power-control.md) |
| Understand the circuit architecture | [Hardware overview](documentation/hardware.md) |
| Print and choose an enclosure | [Enclosures](documentation/enclosures.md) |
| Modify or manufacture the board | [Build and manufacture](documentation/manufacturing.md) |
| Understand revisions and repository layout | [Repository guide](documentation/repository-guide.md) |
| Diagnose a problem | [Troubleshooting](documentation/troubleshooting.md) |
| Propose a change | [Contributing](CONTRIBUTING.md) |

The documentation can also be built as a searchable local site:

```shell
python -m venv .venv
# Windows: .venv\Scripts\activate
# Linux/macOS: source .venv/bin/activate
python -m pip install -r requirements-docs.txt
mkdocs serve
```

## Repository map

```text
pt1/
├── pcba/Rev A2/       KiCad schematic, PCB, and project sources
├── case/Rev A/        Printable STL enclosure variants
├── pinout/            Original pinout generator, data, and source artwork
├── documentation/     Guides, examples, styles, and all new visual assets
├── .github/           Issue forms, pull-request template, and docs automation
├── mkdocs.yml         Documentation-site configuration
└── LICENSES/          CERN-OHL-W-2.0 hardware licence text
```

Current checked-in design revisions are **PCB Rev A2** and **case Rev A**. Source
files are authoritative; generated manufacturing outputs are intentionally not
present in the repository yet.

## Companion software

[Vicuña](https://lab.electrolama.com/project/vicuna) is Electrolama's browser-based
serial monitor and terminal. Its dedicated pt1 mode presents DTR as a clear power
control and RI as a fault indicator instead of exposing generic modem-signal names.

## Project links

- [Published pt1 documentation](https://lab.electrolama.com/project/pt1)
- [Vicuña](https://lab.electrolama.com/project/vicuna)
- [Electrolama](https://electrolama.com)
- [Support and reporting](SUPPORT.md)

## Licence

Hardware source—including schematics, PCB design files, mechanical CAD,
manufacturing files, and other source material required to make or modify the
hardware—is licensed under the [CERN Open Hardware Licence Version 2 — Weakly
Reciprocal](LICENSES/CERN-OHL-W-2.0.txt) (`CERN-OHL-W-2.0`).
