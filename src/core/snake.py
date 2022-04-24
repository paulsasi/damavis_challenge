from typing import Tuple

import src.core.player as player


class Snake(player.Player):

    def __init__(self, snake: Tuple[Tuple[int]]):

        self.snake: Tuple[Tuple[int]] = snake
        if not self.__is_valid():
            raise player.PlayerConstraintsError

        self.head: Tuple[int] = snake[0]

    def __is_valid(self) -> bool:

        # No repetition of snake cells
        if len(set(self.snake)) != len(self.snake):
            return False

        # Snake cells horizontally or vertically adjacent
        for i in range(len(self.snake) - 1):
            snake_part_1_x, snake_part_1_y = self.snake[i]
            snake_part_2_x, snake_part_2_y = self.snake[i + 1]

            distance = (snake_part_2_x - snake_part_1_x) ** 2 + (snake_part_2_y - snake_part_1_y) ** 2
            if distance != 1:
                return False

        return True

    def is_within_limits(self, rows: int, cols: int) -> bool:
        snake_rows, snake_cols = list(zip(*self.snake))

        if min(snake_rows) < 0 or max(snake_rows) > rows - 1:
            return False

        if min(snake_cols) < 0 or max(snake_cols) > cols - 1:
            return False

        return True

    def move_up(self) -> 'Snake':
        head_moved = (self.head[0] - 1, self.head[1])
        snake_moved = (head_moved,) + self.snake[:-1]
        return Snake(snake_moved)

    def move_down(self) -> 'Snake':
        head_moved = (self.head[0] + 1, self.head[1])
        snake_moved = (head_moved,) + self.snake[:-1]
        return Snake(snake_moved)

    def move_left(self) -> 'Snake':
        head_moved = (self.head[0], self.head[1] - 1)
        snake_moved = (head_moved,) + self.snake[:-1]
        return Snake(snake_moved)

    def move_right(self) -> 'Snake':
        head_moved = (self.head[0], self.head[1] + 1)
        snake_moved = (head_moved,) + self.snake[:-1]
        return Snake(snake_moved)

    def __eq__(self, __o: object) -> bool:
        return self.snake == __o.snake
