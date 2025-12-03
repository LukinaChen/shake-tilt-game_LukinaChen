import neopixel
import board
import time

# Initialize NeoPixel (1 LED connected to D6)
pixel = neopixel.NeoPixel(board.D6, 1, brightness=0.3, auto_write=True)

def set_color(color):
    """
    Set the NeoPixel to a specific color.
    Example:
        set_color((255, 0, 0)) -> Red
        set_color((0, 255, 0)) -> Green
        set_color((0, 0, 255)) -> Blue
    """
    pixel[0] = color

def off():
    """
    Turn off the NeoPixel.
    """
    pixel[0] = (0, 0, 0)

def flash(color, duration=0.2):
    """
    Flash the NeoPixel once.
    Args:
        color (tuple): (R, G, B)
        duration (float): time in seconds before turning off
    Example:
        flash((255, 255, 0), 0.3) -> Flash yellow for 0.3 seconds
    """
    pixel[0] = color
    time.sleep(duration)
    pixel[0] = (0, 0, 0)
