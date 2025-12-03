# ==========================================
# check_move.py — returns exact reason of failure
# ==========================================

import time
from motion_utils import detect_move

# Backend extra reaction time (hidden from user)
TIME_BUFFER = 0.3


def check_player_move(expected_move, time_limit):
    """
    Checks the player's action and returns:
        "success"  → correct move
        "wrong"    → wrong move detected
        "timeout"  → time expired
    """

    start = time.monotonic()

    # Backend secret extended time
    allowed_time = time_limit + TIME_BUFFER

    while True:
        move = detect_move()

        # SUCCESS
        if move == expected_move:
            return "success"

        # WRONG MOVE
        if move != "none" and move != expected_move:
            return "wrong"

        # TIMEOUT
        if time.monotonic() - start > allowed_time:
            return "timeout"

        time.sleep(0.01)
