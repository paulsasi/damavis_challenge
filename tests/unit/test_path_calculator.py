import src.path_calculator as path_calculator
import src.board as board
import src.snake as snake


def test_available_paths_1():
    input_board = board.Board(
        nrows=4,
        ncols=3,
        player_possition=snake.Snake(((2, 2), (3, 2), (3, 1), (3, 0), (2, 0), (1, 0), (0, 0)))
    )

    input_depth = 3

    output = 7

    assert path_calculator.available_paths(input_board, input_depth) == output


def test_available_paths_2():
    input_board = board.Board(
        nrows=2,
        ncols=3,
        player_possition=snake.Snake(((0, 2), (0, 1), (0, 0), (1, 0), (1, 1), (1, 2)))
    )

    input_depth = 10

    output = 1

    assert path_calculator.available_paths(input_board, input_depth) == output


def test_available_paths_3():
    input_board = board.Board(
        nrows=10,
        ncols=10,
        player_possition=snake.Snake(((5, 5), (5, 4), (4, 4), (4, 5)))
    )

    input_depth = 4

    output = 81

    assert path_calculator.available_paths(input_board, input_depth) == output


def test_available_paths_5():
    input_board = board.Board(
        nrows=5,
        ncols=5,
        player_possition=snake.Snake(((0, 0), (0, 1), (1, 1), (1, 0), (2, 0)))
    )

    input_depth = 4

    output = 0

    assert path_calculator.available_paths(input_board, input_depth) == output
