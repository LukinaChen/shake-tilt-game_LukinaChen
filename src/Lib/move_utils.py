import random

# All available moves from motion_utils
MOVE_LIST = [
    "tilt_left",
    "tilt_right",
    "tilt_forward",
    "tilt_back",
    "shake"
]

def moves_for_level(difficulty, level):
    """
    Generate move sequence based on:
    - difficulty
    - level number
    - allowed move count rules

    Returns: list of move strings
    """

    # RULE SET
    if difficulty == "Easy":
        move_count = 1
        time_limit = 2.0

    elif difficulty == "Medium":
        time_limit = 1.2
        move_count = 1 if level <= 5 else 2

    else:  # Hard
        time_limit = 0.7
        if level <= 3:
            move_count = 1
        elif level <= 7:
            move_count = 2
        else:
            move_count = 3

    # RANDOMLY GENERATE MOVES
    move_list = [random.choice(MOVE_LIST) for _ in range(move_count)]

    return move_list, time_limit
