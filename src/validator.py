from typing import List, Tuple
import json


class ValidationError(Exception):
    """Raises when an input does not fullfill a constraint"""


def validate_board(board: str) -> Tuple[int]:
    try:
        input_args_board = tuple(json.loads(board))

        if len(input_args_board) != 2:
            raise ValidationError

        if any([isinstance(el, float) for el in input_args_board]):
            raise ValidationError

        BOARD_ROWS__THRESHOLD_LOWER = 1
        BOARD_ROWS__THRESHOLD_UPPER = 10
        if not (BOARD_ROWS__THRESHOLD_LOWER <= input_args_board[0] <= BOARD_ROWS__THRESHOLD_UPPER):
            raise ValidationError

        BOARD_COLS_THRESHOLD_LOWER = 1
        BOARD_COLS_THRESHOLD_UPPER = 10
        if not (BOARD_COLS_THRESHOLD_LOWER <= input_args_board[1] <= BOARD_COLS_THRESHOLD_UPPER):
            raise ValidationError

        return input_args_board

    except (json.decoder.JSONDecodeError, ValidationError):
        raise ValidationError("Input board does not fullfill the constraints.")


def validate_depth(depth: str) -> int:
    pass


def validate_snake(snake: str) -> Tuple[int]:
    pass
