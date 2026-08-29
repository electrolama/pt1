"""Build the self-contained, light-mode 6 x 4 inch pt1 postcard SVG.

The PDF is exported from the generated SVG with Inkscape so the SVG remains the
editable source of truth.
"""

from __future__ import annotations

import base64
from html import escape
from pathlib import Path

import qrcode
from qrcode.constants import ERROR_CORRECT_Q


ROOT = Path(__file__).resolve().parents[2]
OUTPUT = Path(__file__).with_name("pt1-postcard-6x4.svg")
MASCOT = ROOT / "documentation" / "assets" / "images" / "llama-power.png"
GET_STARTED_URL = "https://lab.electrolama.com/project/pt1"


def data_uri(path: Path) -> str:
    encoded = base64.b64encode(path.read_bytes()).decode("ascii")
    return f"data:image/png;base64,{encoded}"


def qr_path(url: str, x: float, y: float, size: float) -> str:
    code = qrcode.QRCode(
        version=None,
        error_correction=ERROR_CORRECT_Q,
        box_size=1,
        border=4,
    )
    code.add_data(url)
    code.make(fit=True)
    matrix = code.get_matrix()
    modules = len(matrix)
    scale = size / modules
    commands: list[str] = []
    for row, values in enumerate(matrix):
        for column, dark in enumerate(values):
            if dark:
                commands.append(
                    f"M{x + column * scale:.4f},{y + row * scale:.4f}"
                    f"h{scale:.4f}v{scale:.4f}h-{scale:.4f}z"
                )
    return "".join(commands)


def main() -> None:
    mascot_uri = data_uri(MASCOT)
    qr = qr_path(GET_STARTED_URL, x=1382, y=757, size=286)
    url = escape(GET_STARTED_URL)

    svg = f'''<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<svg xmlns="http://www.w3.org/2000/svg"
     xmlns:xlink="http://www.w3.org/1999/xlink"
     width="6in" height="4in" viewBox="0 0 1800 1200">
  <title>pt1 open-hardware USB debugging postcard</title>
  <desc>A light-mode 6 by 4 inch postcard introducing pt1 with a QR code linking to the getting-started documentation.</desc>
  <defs>
    <linearGradient id="paper" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fffdf7"/>
      <stop offset="1" stop-color="#f5ecd9"/>
    </linearGradient>
    <linearGradient id="mint" x1="0" y1="0" x2="0" y2="1">
      <stop offset="0" stop-color="#eafafb"/>
      <stop offset="1" stop-color="#d9f1ef"/>
    </linearGradient>
    <filter id="soft-glow" x="-50%" y="-50%" width="200%" height="200%">
      <feGaussianBlur stdDeviation="12"/>
    </filter>
    <clipPath id="page-clip"><rect width="1800" height="1200"/></clipPath>
  </defs>

  <g clip-path="url(#page-clip)">
    <rect width="1800" height="1200" fill="url(#paper)"/>

    <!-- Pale circuit-board texture -->
    <g fill="none" stroke="#9cd8d9" stroke-width="4" opacity="0.34">
      <path d="M0 142h126l48 48h112"/><circle cx="286" cy="190" r="10" fill="#fffdf7"/>
      <path d="M0 846h104l54-54h142"/><circle cx="300" cy="792" r="10" fill="#fffdf7"/>
      <path d="M709 0v94l-54 54v103"/><circle cx="655" cy="251" r="10" fill="#fffdf7"/>
      <path d="M1800 228h-100l-45 45h-87"/><circle cx="1568" cy="273" r="10" fill="#fffdf7"/>
      <path d="M1800 1051h-123l-46-46h-78"/><circle cx="1553" cy="1005" r="10" fill="#fffdf7"/>
    </g>

    <!-- Left mascot panel -->
    <rect x="34" y="34" width="892" height="1132" rx="48" fill="#b98b23" opacity="0.12"/>
    <rect x="24" y="24" width="892" height="1132" rx="48" fill="url(#mint)" stroke="#c99511" stroke-width="4"/>
    <g font-family="Arial, Helvetica, sans-serif" fill="#141820">
      <text x="82" y="105" font-size="28" font-weight="800" letter-spacing="5" fill="#087d8b">OPEN HARDWARE  /  PCB REV A2</text>
      <text x="72" y="286" font-size="214" font-weight="900" letter-spacing="-14">pt1</text>
      <path d="M80 325H424" stroke="#ffc928" stroke-width="15" stroke-linecap="round"/>
      <path d="M520 260l27-49-6 39h30l-46 62 13-46z" fill="#ffc928" stroke="#141820" stroke-width="3" stroke-linejoin="round"/>
      <text x="82" y="382" font-size="43" font-weight="900" letter-spacing="0.5">POWER. SERIAL. USB. REPEAT.</text>
      <text x="84" y="427" font-size="27" fill="#4c5159">A pocket-sized bring-up bench for stubborn hardware.</text>
    </g>

    <ellipse cx="488" cy="1048" rx="280" ry="42" fill="#b98b23" opacity="0.18" filter="url(#soft-glow)"/>
    <image x="116" y="405" width="700" height="700" preserveAspectRatio="xMidYMid meet" xlink:href="{mascot_uri}"/>

    <g font-family="Arial, Helvetica, sans-serif" font-size="22" font-weight="800" fill="#141820">
      <rect x="70" y="1037" width="176" height="64" rx="32" fill="#ffffff" stroke="#8bcfd3" stroke-width="3"/>
      <circle cx="101" cy="1069" r="12" fill="#13bed2"/><text x="124" y="1077">USB HUB</text>
      <rect x="260" y="1037" width="151" height="64" rx="32" fill="#ffffff" stroke="#ef9bbe" stroke-width="3"/>
      <circle cx="291" cy="1069" r="12" fill="#e52b82"/><text x="314" y="1077">UART</text>
      <rect x="425" y="1037" width="240" height="64" rx="32" fill="#ffffff" stroke="#e7bd43" stroke-width="3"/>
      <circle cx="456" cy="1069" r="12" fill="#ffc928"/><text x="479" y="1077">SWITCHED 5 V</text>
      <rect x="679" y="1037" width="171" height="64" rx="32" fill="#ffffff" stroke="#aeb2b7" stroke-width="3"/>
      <circle cx="710" cy="1069" r="12" fill="#ffffff" stroke="#141820" stroke-width="3"/><text x="733" y="1077">FAULT</text>
    </g>

    <!-- Right information card -->
    <rect x="965" y="44" width="807" height="1122" rx="48" fill="#b98b23" opacity="0.13"/>
    <rect x="952" y="24" width="807" height="1122" rx="48" fill="#ffffff" stroke="#dccaa3" stroke-width="4"/>
    <g font-family="Arial, Helvetica, sans-serif" fill="#141820">
      <text x="1012" y="103" font-size="27" font-weight="800" letter-spacing="4" fill="#9b6400">ONE-CABLE LAB MULTITOOL</text>
      <text x="1010" y="180" font-size="54" font-weight="900" letter-spacing="-1">Bring up boards.</text>
      <text x="1010" y="239" font-size="54" font-weight="900" letter-spacing="-1">Lose the spaghetti.</text>
      <text x="1014" y="301" font-size="27" fill="#4c5159">Connect a target, open its console, cycle power,</text>
      <text x="1014" y="338" font-size="27" fill="#4c5159">and catch a fault through one host USB-C cable.</text>

      <g font-size="21" font-weight="800">
        <rect x="1012" y="389" width="310" height="60" rx="20" fill="#dff7fa" stroke="#91dce5" stroke-width="2"/>
        <circle cx="1043" cy="419" r="11" fill="#13bed2"/><text x="1067" y="427">3 external USB ports</text>
        <rect x="1340" y="389" width="350" height="60" rx="20" fill="#fde5ef" stroke="#f1a3c4" stroke-width="2"/>
        <circle cx="1371" cy="419" r="11" fill="#e52b82"/><text x="1395" y="427">Logic-level UART</text>
        <rect x="1012" y="467" width="310" height="60" rx="20" fill="#fff3c9" stroke="#e7bd43" stroke-width="2"/>
        <circle cx="1043" cy="497" r="11" fill="#ffc928"/><text x="1067" y="505">DTR power control</text>
        <rect x="1340" y="467" width="350" height="60" rx="20" fill="#f1eee7" stroke="#c9c1b2" stroke-width="2"/>
        <circle cx="1371" cy="497" r="11" fill="#ffffff" stroke="#141820" stroke-width="2"/><text x="1395" y="505">RI fault status</text>
      </g>

      <path d="M1012 585H1692" stroke="#d8c8a9" stroke-width="3"/>
      <text x="1012" y="648" font-size="30" font-weight="900" letter-spacing="3">GET STARTED</text>
      <text x="1012" y="695" font-size="23" fill="#4c5159">Three moves from workbench to first signal:</text>

      <g font-size="23" font-weight="700">
        <circle cx="1042" cy="760" r="23" fill="#13bed2"/><text x="1035" y="768">1</text>
        <text x="1080" y="752">Connect host USB-C</text><text x="1080" y="783" font-size="20" font-weight="400" fill="#646870">Power and data, one cable.</text>
        <circle cx="1042" cy="851" r="23" fill="#e52b82"/><text x="1035" y="859" fill="#ffffff">2</text>
        <text x="1080" y="843">Wire target + UART</text><text x="1080" y="874" font-size="20" font-weight="400" fill="#646870">UART + switched 5 V.</text>
        <circle cx="1042" cy="942" r="23" fill="#ffc928"/><text x="1035" y="950">3</text>
        <text x="1080" y="934">Open console + iterate</text><text x="1080" y="965" font-size="20" font-weight="400" fill="#646870">Watch, reset, recover, repeat.</text>
      </g>

      <text x="1382" y="720" font-size="24" font-weight="900" letter-spacing="2">SCAN THE GUIDE</text>
      <text x="1382" y="1090" font-size="18" font-family="Consolas, monospace" fill="#646870">lab.electrolama.com/project/pt1</text>
    </g>

    <!-- QR card and vector QR -->
    <rect x="1362" y="737" width="326" height="326" rx="22" fill="#ffffff" stroke="#141820" stroke-width="4"/>
    <path d="{qr}" fill="#141820" shape-rendering="crispEdges"/>

    <!-- Print-safe border and sparks -->
    <rect x="13" y="13" width="1774" height="1174" rx="42" fill="none" stroke="#c99511" stroke-width="4"/>
    <path d="M867 111l30 0-21 46h29l-52 70 15-55h-25z" fill="#ffc928" stroke="#141820" stroke-width="2"/>
    <path d="M882 821l26 0-18 40h25l-46 62 14-48h-23z" fill="#e52b82"/>
  </g>

  <metadata>QR destination: {url}</metadata>
</svg>
'''
    OUTPUT.write_text(svg, encoding="utf-8", newline="\n")
    print(OUTPUT)


if __name__ == "__main__":
    main()
