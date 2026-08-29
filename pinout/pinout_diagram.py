###########################################
#
# Example script to build a
# pinout diagram. Includes basic
# features and convenience classes.
#
###########################################

from pinout.core import Group, Image
from pinout.components.layout import Diagram_2Rows
from pinout.components.pinlabel import PinLabelGroup, PinLabel
from pinout.components.text import TextBlock
from pinout.components import leaderline as lline
from pinout.components.legend import Legend


# Import data for the diagram
import data

# Create a new diagram
# The Diagram_2Rows class provides 2 panels,
# 'panel_01' and 'panel_02', to insert components into.
diagram = Diagram_2Rows(800, 1200, 1075, "diagram")

# Add a stylesheet
diagram.add_stylesheet("styles.css", embed=True)

# Create a group to hold the pinout-diagram components.
graphic = diagram.panel_01.add(Group(202, 50))

# Add and embed an image
hardware = graphic.add(Image("board.png", embed=True))

# Power LED
hardware.add_coord("led_pwr", 225, 350)
graphic.add(
    PinLabel(
        content="Power LED",
        x=hardware.coord("led_pwr").x,
        y=hardware.coord("led_pwr").y,
        tag="led_pwr",
        body={"x": 207, "y": 0},
        #leaderline={"direction": "vh"},
    )
)

# Right Header
hardware.add_coord("vcc", 365, 520)
graphic.add(
    PinLabelGroup(
        x=hardware.coord("vcc").x,
        y=hardware.coord("vcc").y,
        label_start=(61, 0),
        pin_pitch=(0, 52),
        label_pitch=(0, 52),
        labels=data.right_header,
    )
)

# USB Upstream
hardware.add_coord("usb_up", 160, 900)
graphic.add(
    PinLabel(
        content="USB_UP",
        x=hardware.coord("usb_up").x,
        y=hardware.coord("usb_up").y,
        tag="usb_u",
        body={"x": 197, "y": 0},
        scale=(-1, 1),
        #leaderline={"direction": "vh"},
    )
)

# USB Port 2
hardware.add_coord("usb_p2", 50, 400)
graphic.add(
    PinLabel(
        content="USB_P2",
        x=hardware.coord("usb_p2").x,
        y=hardware.coord("usb_p2").y,
        tag="usb_d",
        body={"x": 87, "y": 0},
        scale=(-1, 1),
        #leaderline={"direction": "vh"},
    )
)

# USB Port 1
hardware.add_coord("usb_p1", 130, 170)
graphic.add(
    PinLabel(
        content="USB_P1",
        x=hardware.coord("usb_p1").x,
        y=hardware.coord("usb_p1").y,
        tag="usb_d",
        body={"x":167, "y": 0},
        scale=(-1, 1),
        #leaderline={"direction": "vh"},
    )
)

# Create a title and description text-blocks
title_block = diagram.panel_02.add(
    TextBlock(
        data.title,
        x=20,
        y=30,
        line_height=18,
        tag="panel title_block",
    )
)
diagram.panel_02.add(
    TextBlock(
        data.description,
        x=20,
        y=49,
        width=title_block.width,
        height=diagram.panel_02.height - title_block.height,
        line_height=18,
        tag="panel text_block",
    )
)

# Create a legend
legend = diagram.panel_02.add(
    Legend(
        data.legend,
        x=450,
        y=15,
        max_height=100,
    )
)

# Export the diagram via commandline:
# >>> py -m pinout.manager --export pinout_diagram.py diagram.svg
