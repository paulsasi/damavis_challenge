from enum import Enum
from typing import List

import src.core.player as player


class BoardPossitionError(Exception):
    """Raises when the possition of the player in the board violates any constraint"""


class Board:

    def __init__(self, nrows: int, ncols: int, player_possition: player.Player):

        self.nrows: int = nrows
        self.ncols: int = ncols

        self._player_possition: player.Player = player_possition
        if not self.__is_valid():
            raise BoardPossitionError

    def __is_valid(self) -> bool:

        if self._player_possition.is_within_limits(self.nrows, self.ncols):
            return True
        return False

    def move_player_up(self) -> 'Board':
        try:
            player_new_possition = self._player_possition.move_up()
            return Board(self.nrows, self.ncols, player_new_possition)
        except (player.PlayerConstraintsError, BoardPossitionError):
            raise BoardPossitionError

    def move_player_down(self) -> 'Board':
        try:
            player_new_possition = self._player_possition.move_down()
            return Board(self.nrows, self.ncols, player_new_possition)
        except player.PlayerConstraintsError:
            raise BoardPossitionError

    def move_player_left(self) -> 'Board':
        try:
            player_new_possition = self._player_possition.move_left()
            return Board(self.nrows, self.ncols, player_new_possition)
        except player.PlayerConstraintsError:
            raise BoardPossitionError

    def move_player_right(self) -> 'Board':
        try:
            player_new_possition = self._player_possition.move_right()
            return Board(self.nrows, self.ncols, player_new_possition)
        except player.PlayerConstraintsError:
            raise BoardPossitionError
