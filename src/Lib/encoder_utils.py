import digitalio
import board
import time

# ===========================================
#  ROTARY ENCODER (Rotate)
# ===========================================
class SimpleEncoder:
    def __init__(self, pin_a=board.D1, pin_b=board.D2):
        self.pin_a = digitalio.DigitalInOut(pin_a)
        self.pin_b = digitalio.DigitalInOut(pin_b)

        self.pin_a.switch_to_input(pull=digitalio.Pull.UP)
        self.pin_b.switch_to_input(pull=digitalio.Pull.UP)

        self.last_state = (self.pin_a.value, self.pin_b.value)

    def update(self):
        current = (self.pin_a.value, self.pin_b.value)
        if current != self.last_state:
            a_last, b_last = self.last_state
            a_now, b_now = current
            self.last_state = current

            if a_last == a_now and b_now != b_last:
                return "rotate_cw"
            if b_last == b_now and a_now != a_last:
                return "rotate_ccw"

        return None


# ===========================================
#  ENCODER BUTTON (SW → D9)
# ===========================================
enc_button = digitalio.DigitalInOut(board.D9)
enc_button.switch_to_input(pull=digitalio.Pull.UP)

_last_enc_btn = False

def encoder_button_pressed_once():
    global _last_enc_btn

    current = not enc_button.value  # True when pressed

    if current and not _last_enc_btn:
        _last_enc_btn = current
        return True

    _last_enc_btn = current
    return False
