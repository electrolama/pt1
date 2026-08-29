"""Safely power-cycle a pt1 target and monitor its load-switch fault signal."""

from __future__ import annotations

import argparse
import sys
import time

import serial


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Power-cycle a target through pt1 using DTR and monitor RI."
    )
    parser.add_argument("--port", required=True, help="pt1 serial port, for example COM12")
    parser.add_argument("--baud", type=int, default=115200, help="UART baud rate")
    parser.add_argument(
        "--cycles", type=int, default=1, help="number of on/off cycles (default: 1)"
    )
    parser.add_argument(
        "--on-seconds", type=float, default=4.0, help="powered duration per cycle"
    )
    parser.add_argument(
        "--off-seconds", type=float, default=1.0, help="off duration between cycles"
    )
    parser.add_argument(
        "--poll-seconds", type=float, default=0.1, help="fault polling interval"
    )
    args = parser.parse_args()

    if args.cycles < 1:
        parser.error("--cycles must be at least 1")
    for name in ("on_seconds", "off_seconds", "poll_seconds"):
        if getattr(args, name) < 0:
            parser.error(f"--{name.replace('_', '-')} cannot be negative")
    return args


def set_power(device: serial.Serial, enabled: bool) -> None:
    """pt1 uses deasserted DTR for on and asserted DTR for off."""
    device.dtr = not enabled
    print(f"power {'ON' if enabled else 'OFF'} (DTR={device.dtr})")


def monitor_for_fault(
    device: serial.Serial, duration: float, poll_interval: float
) -> bool:
    deadline = time.monotonic() + duration
    while time.monotonic() < deadline:
        if device.ri:
            return True
        time.sleep(poll_interval)
    return False


def main() -> int:
    args = parse_args()
    device = serial.Serial()
    device.port = args.port
    device.baudrate = args.baud
    device.timeout = 0
    device.dtr = True  # request the safe off state before opening

    try:
        print(f"opening {args.port} at {args.baud} baud")
        device.open()
        set_power(device, enabled=False)  # drivers can alter DTR during open

        for cycle in range(1, args.cycles + 1):
            print(f"cycle {cycle}/{args.cycles}")
            set_power(device, enabled=True)

            if monitor_for_fault(device, args.on_seconds, args.poll_seconds):
                print("FAULT: RI asserted; disabling switched power", file=sys.stderr)
                set_power(device, enabled=False)
                return 2

            set_power(device, enabled=False)
            if cycle < args.cycles:
                time.sleep(args.off_seconds)

        return 0
    except serial.SerialException as exc:
        print(f"serial error: {exc}", file=sys.stderr)
        return 1
    except KeyboardInterrupt:
        print("interrupted", file=sys.stderr)
        return 130
    finally:
        if device.is_open:
            try:
                set_power(device, enabled=False)
            finally:
                device.close()
                print("port closed; power left off")


if __name__ == "__main__":
    raise SystemExit(main())

