import board
import busio
import displayio
import terminalio
from adafruit_display_text import label
import i2cdisplaybus
import adafruit_displayio_ssd1306

# Release displays first
displayio.release_displays()

# Create I2C bus for display (this works for your board)
i2c = busio.I2C(board.SCL, board.SDA)

# Create display interface
display_bus = i2cdisplaybus.I2CDisplayBus(i2c, device_address=0x3C)
display = adafruit_displayio_ssd1306.SSD1306(display_bus, width=128, height=64)

def show_text(lines):
    """
    Display multiple lines of text on the OLED screen.
    """
    group = displayio.Group()
    y = 10

    for txt in lines:
        text_area = label.Label(
            terminalio.FONT,
            text=txt,
            color=0xFFFFFF,
            x=0,
            y=y,
        )
        group.append(text_area)
        y += 14

    # IMPORTANT: This must be INSIDE the function
    display.root_group = group
