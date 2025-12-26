FIRMWARE

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.extensions.neopixel import NeoPixel

keyboard = KMKKeyboard()

# ─────────────────────────────
# MATRIX CONFIG
# ─────────────────────────────

keyboard.col_pins = (
    board.GP0,   # COL0
    board.GP27,  # COL1
    board.GP28,  # COL2
    board.GP29,  # COL3
)

keyboard.row_pins = (
    board.GP3,   # ROW0
    board.GP4,   # ROW1
    board.GP2,   # ROW2
    board.GP1,   # ROW3
)

keyboard.diode_orientation = DiodeOrientation.COLUMNS

# ─────────────────────────────
# KEYMAP (4 × 4)
# Matches your PCB layout
# ─────────────────────────────

keyboard.keymap = [
    [
        KC.A, KC.A, KC.A, KC.A,
        KC.A, KC.A, KC.A, KC.A,
        KC.A, KC.A, KC.A, KC.A,
        KC.A, KC.A, KC.A, KC.A,
    ]
]

# ─────────────────────────────
# RGB (SK6812)
# ─────────────────────────────

rgb = NeoPixel(
    pin=board.GP26,   # LIGHTS pin
    num_pixels=16,    # change if needed
    brightness=0.3,
    auto_write=True,
)

keyboard.extensions.append(rgb)


# ───────────────── OLED DISPLAY ─────────────────
display = Display(
    display_type='SSD1306',
    width=128,
    height=32,
    flip=False,
)

# placeholders (updated from PC)
cpu = TextEntry(text='🖥 CPU: --%', x=0, y=0)
ram = TextEntry(text='🧠 RAM: --%', x=0, y=8)
gpu = TextEntry(text='🎮 GPU: --%', x=64, y=0)
disk = TextEntry(text='💾 C: --%', x=64, y=8)

display.entries = [cpu, ram, gpu, disk]
keyboard.extensions.append(display)


# Optional: startup color
rgb.fill((0, 50, 255))

# ─────────────────────────────
# START
# ─────────────────────────────

if __name__ == '__main__':
    keyboard.go()