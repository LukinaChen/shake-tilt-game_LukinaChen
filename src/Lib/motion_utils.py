# ================================
# Motion Utils (Instant Response)
# ================================

import adafruit_adxl34x
from display_utils import i2c

# Previous filtered acceleration
prev_x = 0
prev_y = 0
prev_z = 0

# Faster reaction, lighter filtering
LPF_ALPHA = 1.0      # previously 0.3 → now reacts very fast
TILT_THRESHOLD = 0.9  # gentle movement triggers
SHAKE_THRESHOLD = 0.9 # shake sensitivity increased

accelerometer = adafruit_adxl34x.ADXL345(i2c)


# ============ LOW-PASS FILTER ============
def get_acceleration():
    global prev_x, prev_y, prev_z

    x, y, z = accelerometer.acceleration

    # Lighter smoothing → faster detection
    prev_x = prev_x * (1 - LPF_ALPHA) + x * LPF_ALPHA
    prev_y = prev_y * (1 - LPF_ALPHA) + y * LPF_ALPHA
    prev_z = prev_z * (1 - LPF_ALPHA) + z * LPF_ALPHA

    return prev_x, prev_y, prev_z


# ============ TILT LEFT / RIGHT ============
def detect_left_right():
    x, y, z = get_acceleration()

    if x > TILT_THRESHOLD:
        return "tilt_left"
    if x < -TILT_THRESHOLD:
        return "tilt_right"

    return None


# ============ TILT FORWARD / BACK ============
def detect_front_back():
    x, y, z = get_acceleration()

    if y < -TILT_THRESHOLD:
        return "tilt_forward"
    if y > TILT_THRESHOLD:
        return "tilt_back"

    return None


# ============ SHAKE (instant) ============
def detect_shake():
    x, y, z = accelerometer.acceleration

    dx = abs(x - prev_x)
    dy = abs(y - prev_y)
    dz = abs(z - prev_z)

    # MUCH less filtered → very responsive shake
    return (dx + dy + dz) > SHAKE_THRESHOLD


# ============ MAIN MOVE DETECTOR ============
def detect_move():
    # Priority: tilt → shake
    mv = detect_left_right()
    if mv:
        return mv

    mv = detect_front_back()
    if mv:
        return mv

    if detect_shake():
        return "shake"

    return "none"
