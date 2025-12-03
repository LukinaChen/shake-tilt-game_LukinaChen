# =============================
# MAIN GAME LAUNCHER (code.py)
# =============================

import time
from game_state import run_game_step

while True:
    try:
        # Run one step of state machine
        run_game_step()

        # Small delay keeps CPU stable
        time.sleep(0.02)

    except Exception as e:
        # Prevent the board from freezing
        print("ERROR:", e)
        time.sleep(1)
