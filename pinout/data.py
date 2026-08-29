legend = [
    ("USB (Upstream)", "usb_u"),
    ("USB (Downstream)", "usb_d"),
    ("Power LED", "led_pwr"),
    ("UART", "uart"),
    ("Power", "pwr"),
    ("Ground", "gnd"),
]

# Pinlabels

right_header = [
    [
        ("VBUS_SW", "pwr"),
    ],
    [
        ("RX_IN", "uart"),
    ],
    [
        ("TX_OUT", "uart"),
    ],
    [
        ("USB_P3_N", "usb_d"),
    ],
    [
        ("USB_P3_P", "usb_d"),
    ],
    [
        ("GND", "gnd"),
    ],
]


# Text

title = "<tspan class='h1'>pt1</tspan>"

description = """<tspan class='italic strong'>electrolama.com/pt1</tspan>
3-port USB 2.0 Hub with CH343 USB-Serial Converter
and a USB Load switch, controlled via serial port, with
TVS and overcurrent protection and short circuit alert.
"""
