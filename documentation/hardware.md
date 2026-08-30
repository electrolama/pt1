# Hardware overview

pt1 is intentionally a composition of well-understood hardware blocks. The value
comes from putting them on one narrow board and connecting the serial bridge's modem
signals to the protected power path.

## Functional architecture

```text
                       ┌──────────────────────────────┐
Host USB-C ───────────▶│ SL2.1A four-port USB 2.0 hub │
                       └──────┬──────┬──────┬─────────┘
                              │      │      │
                         USB-C│ USB-A│      │header USB D+/D−
                              │      │      │
                              │  switched  switched
                              │    5 V       5 V
                              │      ▲        ▲
                              │      └───┬────┘
                              │          │
                              │   RT9742 load switch
                              │     ▲ enable  │ fault
                              │     │         ▼
                              └── CH343P USB-to-UART
                                      │
                                  TX / RX header
```

The diagram is conceptual. Use the KiCad schematic for net-level truth.

## USB hub

The SL2.1A supplies four downstream USB 2.0 ports:

1. one physical downstream USB-C connector;
2. one physical downstream USB-A connector;
3. one USB D+/D− pair on the six-pin header; and
4. the onboard CH343P serial bridge.

This explains why the product is described both as a three-port external hub and a
four-port hub controller. All connectors are USB 2.0 only.

## USB-to-UART bridge

The CH343P provides the header TX/RX console and the DTR/RI signals used by the power
subsystem. pt1 exposes logic-level UART, not ±RS-232 signalling. The hardware does
not need firmware to implement power commands.

## Protected switched power

The RT9742CGJ5 load switch drives the switched USB power domain. Its jobs include:

- host-controlled enable;
- current limiting;
- over-temperature protection; and
- active-low fault reporting.

The load switch is useful protection, not a programmable bench supply. The actual
available current and voltage depend on the complete upstream USB system.

## Control logic

DTR is active-low at the serial API boundary, while the load-switch enable requires
the design's intended polarity. The SN74LVC1G57 single-gate configurable logic
device conditions this path. A startup timing network keeps switched power disabled
briefly while the board initializes.

The load switch's active-low fault signal is connected to the CH343P's active-low RI
input. Serial software therefore normally sees RI asserted during an over-current
or over-temperature condition.

## Protection and indicators

- SRV05-4-P-T7 TVS arrays protect USB data-line groups.
- A ferrite bead and local bulk/decoupling capacitors condition USB power.
- The green `PWR` LED indicates presence of the switched rail.
- USB-C CC resistors identify the relevant connector roles.

## Main components

| Reference | Component | Role |
| --- | --- | --- |
| IC1 | CH343P | USB-to-UART bridge and DTR/RI interface |
| IC2 | SL2.1A | four-port USB 2.0 hub controller |
| IC3 | SN74LVC1G57DBV | configurable control-logic gate |
| IC4 | RT9742CGJ5 | protected current-limited load switch |
| D1, D2 | SRV05-4-P-T7 | USB transient-voltage suppression arrays |
| XT1 | 12 MHz crystal | hub timing reference |
| LED1 | green LED | switched-power indication |

The reference/value pairs above are extracted from the checked-in Rev A2 schematic.
They are not a purchasing BOM; package, tolerance, rating, and approved-alternative
information must be verified from the source before manufacture.

## Mechanical envelope

The published board size is approximately **46 × 18 mm**, with three 2 mm mounting
holes. Printable case variants either expose or omit the header opening, plus an
OOBB-compatible bottom variant. See [Enclosures](enclosures.md).

## Design limits to keep visible

- USB-C does not imply USB 3.x or USB Power Delivery here.
- The header USB pair is electrically more demanding than UART jumper wiring.
- The switched-power LED is an indicator, not a measurement.
- Control-signal polarity is easy to invert in software.
- A target can remain partially powered through other attached interfaces.
- The downstream USB-C power solder jumper must select exactly one source.

