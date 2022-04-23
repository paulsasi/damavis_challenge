from typing import List

from abc import ABC, abstractmethod


class PlayerConstraintsError(Exception):
    """Raises when the player does not fullfill a constraint"""


class Player(ABC):

    @abstractmethod
    def move_up(self) -> 'Player':
        pass

    @abstractmethod
    def move_down(self) -> 'Player':
        pass

    @abstractmethod
    def move_left(self) -> 'Player':
        pass

    @abstractmethod
    def move_right(self) -> 'Player':
        pass
