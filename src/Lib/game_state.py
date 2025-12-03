# ======================================
# Updated Game State Machine (using encoder button)
# ======================================

import time
from display_utils import show_text
from encoder_utils import SimpleEncoder, encoder_button_pressed_once
from pixel_utils import set_color, off
from move_utils import moves_for_level
from check_move import check_player_move

encoder = SimpleEncoder()
state = "START"

difficulty_list = ["Easy", "Medium", "Hard"]
difficulty_index = 0

level = 1
max_levels = 10

moves = []
time_limit = 2.0
move_index = 0


# ======================================
#  START SCREEN
# ======================================
def state_start():
    global state

    show_text([
        "SHAKE & TILT GAME",
        "",
        "Press Encoder",
        "to Start",
        ""
    ])

    while True:
        if encoder_button_pressed_once():
            time.sleep(0.25)
            state = "SELECT_DIFFICULTY"
            return
        time.sleep(0.02)


# ======================================
#  DIFFICULTY SELECT
# ======================================
def state_select_difficulty():
    global state, difficulty_index

    delta = encoder.update()
    if delta == "rotate_cw":
        difficulty_index += 1
    elif delta == "rotate_ccw":
        difficulty_index -= 1

    difficulty_index = max(0, min(2, difficulty_index))
    diff = difficulty_list[difficulty_index]

    show_text([
        "Select Mode:",
        f"> {diff}",
        "Rotate / Press"
    ])

    if encoder_button_pressed_once():
        time.sleep(0.25)
        state = "GAME_READY"


# ======================================
#  RULES + COUNTDOWN
# ======================================
def state_game_ready():
    global state, level

    diff = difficulty_list[difficulty_index]

    # Rules text
    if diff == "Easy":
        rule_line = "1 move each level"
        limit_line = "2.0s limit"
    elif diff == "Medium":
        rule_line = "1-2 moves / L"
        limit_line = "1.2s limit"
    else:
        rule_line = "1-3 moves / L"
        limit_line = "0.7s limit"

    # --- Updated UI with start instruction ---
    show_text([
        f"Mode: {diff}",
        rule_line,
        limit_line,
        "Press to Start"
    ])

    # Wait for encoder press
    while not encoder_button_pressed_once():
        time.sleep(0.05)

    # Countdown
    for t in ["3", "2", "1"]:
        show_text([
            "Starting...",
            "",
            "",
            t,
            ""
        ])
        time.sleep(1)

    show_text(["BEGIN!", "", "", "", ""])
    time.sleep(1)

    level = 1
    state = "PREPARE_LEVEL"



# ======================================
#  LEVEL PREPARATION
# ======================================
def state_prepare_level():
    global state, moves, time_limit

    diff = difficulty_list[difficulty_index]
    moves, time_limit = moves_for_level(diff, level)

    header = f"{diff} L{level}  T:{time_limit:.1f}s"
    divider = "---------------"

    move_line1 = ", ".join(moves[:2]) + ("," if len(moves) > 2 else "")
    move_line2 = ", ".join(moves[2:]) if len(moves) > 2 else ""

    lines = [header, divider, move_line1]
    if move_line2:
        lines.append(move_line2)

    while len(lines) < 5:
        lines.append("")

    show_text(lines)
    time.sleep(2)

    state = "PLAY_LEVEL"


# ======================================
#  PLAY LEVEL
# ======================================
def state_play_level():
    global state, move_index, level

    expected = moves[move_index]

    show_text([
        f"Do: {expected}",
        f"{move_index+1}/{len(moves)}",
        f"Limit {time_limit}s",
        "",
        ""
    ])

    result = check_player_move(expected, time_limit)

    if result == "success":
        set_color((0, 255, 0))
        time.sleep(0.25)
        off()

        move_index += 1

        if move_index >= len(moves):
            move_index = 0
            level += 1

            if level > max_levels:
                state = "GAME_WIN"
            else:
                state = "PREPARE_LEVEL"
        return

    set_color((255, 0, 0))
    time.sleep(0.4)
    off()
    state = "GAME_OVER"


# ======================================
#  GAME OVER
# ======================================
def state_game_over():
    global state, level

    show_text([
        "GAME OVER",
        f"Level {level}",
        "Press Encoder",
        "to Restart",
        ""
    ])

    if encoder_button_pressed_once():
        time.sleep(0.25)
        level = 1
        state = "START"


# ======================================
#  GAME WIN
# ======================================
def state_game_win():
    global state, level

    show_text([
        "YOU WIN!",
        "",
        "",
        "Press Encoder",
        "to Restart"
    ])

    if encoder_button_pressed_once():
        time.sleep(0.25)
        level = 1
        state = "START"


# ======================================
#  MAIN RUN LOOP ENTRY
# ======================================
def run_game_step():
    global state

    if state == "START":
        state_start()
    elif state == "SELECT_DIFFICULTY":
        state_select_difficulty()
    elif state == "GAME_READY":
        state_game_ready()
    elif state == "PREPARE_LEVEL":
        state_prepare_level()
    elif state == "PLAY_LEVEL":
        state_play_level()
    elif state == "GAME_OVER":
        state_game_over()
    elif state == "GAME_WIN":
        state_game_win()
