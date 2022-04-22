from ast import parse
from typing import List, Tuple
import json


class ValidationError(Exception):
    """Raises when an input does not fullfill a constraint"""


def validate_board(board: str) -> Tuple[int]:
    try:
        parsed_board = tuple(json.loads(board))

        if len(parsed_board) != 2:
            raise ValidationError

        if any([isinstance(el, float) for el in parsed_board]):
            raise ValidationError

        BOARD_ROWS__THRESHOLD_LOWER = 1
        BOARD_ROWS__THRESHOLD_UPPER = 10
        if not (BOARD_ROWS__THRESHOLD_LOWER <= parsed_board[0] <= BOARD_ROWS__THRESHOLD_UPPER):
            raise ValidationError

        BOARD_COLS_THRESHOLD_LOWER = 1
        BOARD_COLS_THRESHOLD_UPPER = 10
        if not (BOARD_COLS_THRESHOLD_LOWER <= parsed_board[1] <= BOARD_COLS_THRESHOLD_UPPER):
            raise ValidationError

        return parsed_board

    except (json.decoder.JSONDecodeError, ValidationError):
        raise ValidationError("Input board does not fullfill the constraints.")


def validate_depth(depth: str) -> int:
    try:
        parsed_depth = json.loads(depth)

        if not isinstance(parsed_depth, int):
            raise ValidationError

        DEPTH_THRESHOLD_LOWER = 1
        DEPTH_THRESHOLD_UPPER = 20
        if not(DEPTH_THRESHOLD_LOWER <= parsed_depth <= DEPTH_THRESHOLD_UPPER):
            raise ValidationError

        return parsed_depth
    except (json.decoder.JSONDecodeError, ValidationError):
        raise ValidationError("Input depth does not fullfill the constraints.")


def validate_snake(snake: str) -> Tuple[int]:
    try:
        parsed_snake = json.loads(snake)

        if not all(isinstance(cell, list) for cell in parsed_snake):
            raise ValidationError

        SNAKE_THRESHOLD_LOWER = 3
        SNAKE_THRESHOLD_UPPER = 7
        if not (SNAKE_THRESHOLD_LOWER <= len(parsed_snake) <= SNAKE_THRESHOLD_UPPER):
            raise ValidationError

        if any([len(cell) != 2 for cell in parsed_snake]):
            raise ValidationError

        return parsed_snake

    except (json.decoder.JSONDecodeError, ValidationError):
        raise ValidationError("Input snake does not fullfill the constraints.")
