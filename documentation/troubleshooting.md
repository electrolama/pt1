# Troubleshooting

Troubleshoot from upstream to downstream: host connection, hub, serial bridge,
control state, switched rail, then target. Changing several cables or signals at
once makes USB and power faults much harder to isolate.

## Nothing enumerates

1. Use a known data-capable USB-C cable.
2. Connect pt1 directly to the host rather than through another unpowered hub.
3. Disconnect every downstream device and header wire.
4. Inspect the upstream connector and PCB for damage or debris.
5. Compare behavior on another host port and, if available, another host.
6. Stop if the board heats, smells, or repeatedly trips host-port protection.

## Hub appears but downstream USB does not

- Test one downstream port at a time with a known low-power USB 2.0 device.
- Confirm the affected port has the intended power source.
- For the header port, verify D+/D− have not been swapped and ground is present.
- Replace long or loose flying leads with a controlled short connection.
- Inspect operating-system USB topology and error logs.
- Separate data failure from power failure by measuring safely at the load.

## Serial port does not appear

- Verify the hub itself enumerates; the CH343P is one of its downstream devices.
- Check whether the operating system requires or has blocked a suitable CH343
  driver.
- Disconnect other USB serial adapters to make enumeration changes obvious.
- Inspect device-manager or kernel logs for VID/PID, driver binding, and errors.
- If the CH343 never appears but other hub ports work, investigate the internal hub
  port, bridge power/clocking, and assembly.

## Serial data is unreadable

- Confirm target TX → `RX_IN` and target RX → `TX_OUT`.
- Confirm a common ground.
- Match baud rate, data bits, parity, and stop bits.
- Confirm the target is not using inverted UART or RS-232 voltage levels.
- Check logic-voltage compatibility and signal integrity with appropriate tools.
- Test one direction at a time or perform a safe loopback where appropriate.

## Power state is inverted

pt1's intended API mapping is DTR `False` = power on and DTR `True` = power off.
Check whether the program labels an asserted modem signal rather than exposing the
raw boolean. Observe the PWR LED and measure the rail while explicitly toggling DTR.

## Power changes when the port opens

This is common serial-driver behavior. Configure DTR before open when the library
allows it, write the off state immediately after open, and avoid general-purpose
terminal programs that manage DTR implicitly. See [Power control](power-control.md).

## RI always reports a fault

1. Turn switched power off and disconnect the target.
2. Reopen the serial port and establish the host/library's RI idle polarity.
3. Inspect for a short or unexpectedly heavy load on the switched rail.
4. Allow the load switch to cool.
5. Verify the serial driver actually exposes RI and is not returning a cached or
   unsupported value.
6. If the condition persists unloaded, inspect the fault net and assembly.

## Target remains partly powered when off

Look for a second energy path through:

- UART TX/RX protection structures;
- USB D+/D−;
- a debugger or logic analyser;
- another ground-referenced instrument;
- GPIO connected to another powered board; or
- the downstream USB-C jumper selection.

Disconnect interfaces methodically and measure at the target. Power switching one
rail does not guarantee every external signal becomes high impedance.

## PWR LED is off but the target runs

The target is probably powered through another path, or it has enough stored energy
to continue briefly. The LED only indicates the pt1 switched rail at its indicator
circuit. It does not monitor every target rail.

## Reporting a reproducible issue

Include the information listed in the repository's
[support guide](https://github.com/electrolama/pt1/blob/main/SUPPORT.md) when using
GitHub. For the MkDocs site, the same checklist is reproduced in the
[contributor guide](contributing.md#good-problem-reports).
