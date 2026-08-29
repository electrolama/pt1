# Power control and fault monitoring

<div class="mascot-split">
  <div>
    <img class="mascot" src="../assets/images/llama-power.png" alt="Chibi llama operating the pt1 power control">
  </div>
  <div>
    <p>pt1 reuses the CH343P serial bridge's DTR and RI modem-control signals. There is no command parser or firmware in the power path: the host changes and reads the signals through its serial API.</p>
  </div>
</div>

## Signal truth table

| API-level state | Hardware meaning | pt1 result |
| --- | --- | --- |
| DTR `False` / deasserted | conditioned enable is high | switched power **on** |
| DTR `True` / asserted | conditioned enable is low | switched power **off** |
| RI not asserted | load switch has not reported a fault | normal |
| RI asserted | active-low fault output is active | over-current or over-temperature fault |

The exact boolean presentation of modem inputs can vary between operating systems,
drivers, and libraries. Validate DTR, RI, and PWR LED behavior on the actual host
before relying on it unattended.

## Safe control sequence

1. Configure the serial object with DTR asserted (`True`) before or immediately
   after opening the port.
2. Open the port and explicitly write the power-off state again.
3. Clear stale assumptions about RI and observe its idle state.
4. Deassert DTR (`False`) to enable switched power.
5. Monitor RI for the entire powered interval.
6. If RI indicates a fault, assert DTR (`True`) immediately and record the event.
7. In every exit path—including exceptions and Ctrl+C—leave DTR asserted and close
   the port.

!!! warning "Opening a serial port can change DTR"
    Some drivers and terminal programs assert DTR automatically. pt1 includes a
    short startup delay, but software must still set DTR deliberately. Never assume
    that a closed port, newly opened port, or crashed process implies a particular
    target-power state.

## Python example

Install the dependency:

```shell
python -m pip install pyserial
```

Run the checked-in example:

```shell
python documentation/examples/power_cycle.py --port COM12
```

On Linux or macOS, replace `COM12` with the discovered device path. The example
powers the target, monitors RI, powers it off, waits, and repeats. It defaults to a
safe power-off state on exit.

```python
from serial import Serial

pt1 = Serial()
pt1.port = "COM12"
pt1.baudrate = 115200
pt1.dtr = True          # request power off before open
pt1.open()

try:
    pt1.dtr = True      # make the post-open state explicit
    pt1.dtr = False     # power on
    if pt1.ri:
        pt1.dtr = True  # fault: power off immediately
        raise RuntimeError("pt1 load-switch fault")
finally:
    pt1.dtr = True
    pt1.close()
```

## Integrating with another language

The requirements are deliberately small:

- open the pt1 serial device;
- use the platform's DTR setter;
- use the platform's RI/modem-status reader;
- make state transitions explicit; and
- guarantee an off action during cleanup.

No bytes need to be transmitted for power control. UART data and the DTR/RI control
path can be used independently.

## Fault response

![Chibi llama demonstrating protected fault handling](assets/images/llama-protection.png){ .mascot-float-left }

When RI indicates a fault:

1. disable switched power;
2. disconnect or isolate the target if the condition persists;
3. inspect wiring and expected inrush/load current;
4. allow thermal protection time to recover where relevant;
5. verify there is no second supply or back-power path; and
6. retry only with appropriate bench current limiting and observation.

The PWR LED shows that the switched rail is present. It does not prove that the
target voltage is within tolerance, report current, or replace measurement at the
load.

## Vicuña

[Vicuña](https://lab.electrolama.com/project/vicuna) presents these same signals as
a device-specific power toggle and fault indicator alongside terminal, timestamped
monitor, and binary/hex views. It is the recommended interactive interface when a
custom automation script is unnecessary.
