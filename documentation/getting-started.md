# Getting started

This path assumes you already work comfortably with USB, UART, and target-board
power. It emphasizes the pt1-specific details that can otherwise surprise an
experienced user.

## What you need

- a data-capable USB-C cable from the host to pt1;
- a target whose USB or 5 V input is compatible with the available host power;
- three jumper wires for UART (`TX`, `RX`, and `GND`) if required;
- [Vicuña](https://lab.electrolama.com/project/vicuna) or another serial program;
  and
- optionally, Python 3 plus `pyserial` for automation.

!!! danger "Before applying power"
    Disconnect or reconcile every other source that can power the target. Do not
    allow pt1 and an external supply to fight through a target's USB, header, or
    protection paths. Inspect the downstream USB-C power-selection solder jumper
    and never bridge both selections simultaneously.

## 1. Identify the connections

Use the [pinout diagram](pinout.md) rather than relying on connector position alone.
The upstream USB-C port goes to the host. The USB-A socket and header switched-power
pin are behind the protected load switch. The other downstream USB-C port's power
source depends on its solder-jumper configuration.

## 2. Connect pt1 to the host

Connect only pt1 at first. A healthy board should enumerate a USB 2.0 hub and a
CH343 serial interface. The exact serial-port name is operating-system dependent.

=== "Windows"

    Inspect **Device Manager → Ports (COM & LPT)** and note the new `COM` port.

=== "Linux"

    Compare `ls /dev/ttyUSB* /dev/ttyACM*` before and after connection, or inspect
    the most recent kernel log entries.

=== "macOS"

    Compare `ls /dev/cu.*` before and after connection.

If only the hub appears, stop and work through [Serial port does not
appear](troubleshooting.md#serial-port-does-not-appear).

## 3. Wire UART

With target power off:

- target **TX** → pt1 `RX_IN`;
- target **RX** → pt1 `TX_OUT`; and
- target **GND** → pt1 `GND`.

These are logic-level UART signals, not RS-232 voltage levels. Confirm the target's
logic-voltage compatibility from the schematic and target documentation before
connecting it. Baud rate and framing do not affect the separate DTR/RI power-control
path, but they must match the target for meaningful console data.

## 4. Connect target USB or switched power

Choose one intentional power path:

- connect a USB target to the switched USB-A socket;
- use the header's `VBUS_SW` and `GND`; or
- use the downstream USB-C connector only after confirming its solder-jumper
  selection.

Do not connect the raw USB data pair without a common ground. Preserve D+/D− pairing
and keep flying leads short if using the header USB port.

## 5. Control power

The easiest route is Vicuña's pt1 mode. For a custom integration:

- set DTR to `False` to turn switched power **on**;
- set DTR to `True` to turn switched power **off**; and
- read RI; an asserted state normally means the load switch reports a fault.

Read [Power control](power-control.md) before unattended operation. Serial-port
open/close behavior varies, and some programs assert DTR automatically.

## 6. Verify before trusting a rig

Perform these tests with a non-critical target:

1. Verify the PWR LED follows the intended switched state.
2. Confirm the target fully loses power when switched off; watch for back-powering
   through UART or another cable.
3. Confirm the serial console recovers after several power cycles.
4. Exercise fault handling with a safe, current-limited test setup appropriate to
   your bench procedures.
5. Confirm the control program leaves power off after normal exit, exception, and
   interruption.

## Next

- [Pinout and connections](pinout.md)
- [Power-control API and example](power-control.md)
- [Troubleshooting](troubleshooting.md)

