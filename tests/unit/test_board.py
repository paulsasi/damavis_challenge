import src.board as board
import src.snake as snake


def test_board_init_1():
    input_player_possition = snake.Snake(((2, 0), (3, 0), (4, 0)))
    input_nrows = 4
    input_ncols = 6

    try:
        result_board = board.Board(input_nrows, input_ncols, input_player_possition)
        assert 0 == 1

    except board.BoardPossitionError:
        assert 0 == 0


def test_board_init_2():
    input_player_possition = snake.Snake(((0, 6), (0, 5), (0, 4)))
    input_nrows = 6
    input_ncols = 4

    try:
        result_board = board.Board(input_nrows, input_ncols, input_player_possition)
        assert 0 == 1

    except board.BoardPossitionError:
        assert 0 == 0


def test_board_init_3():
    input_player_possition = snake.Snake(((1, -1), (2, -1), (3, -1)))
    input_nrows = 6
    input_ncols = 4

    try:
        result_board = board.Board(input_nrows, input_ncols, input_player_possition)
        assert 0 == 1

    except board.BoardPossitionError:
        assert 0 == 0


def test_board_init_5():
    input_player_possition = snake.Snake(((-2, 2), (-2, 1), (-2, 0)))
    input_nrows = 6
    input_ncols = 4

    try:
        result_board = board.Board(input_nrows, input_ncols, input_player_possition)
        assert 0 == 1

    except board.BoardPossitionError:
        assert 0 == 0


def test_board_init_6():
    input_player_possition = snake.Snake(((5, 5), (5, 4), (4, 4), (4, 3)))
    input_nrows = 6
    input_ncols = 6

    result = board.Board(input_nrows, input_ncols, input_player_possition)


def test_board_move_player_up_1():
    input_board = board.Board(
                                nrows=3,
                                ncols=3,
                                player_possition=snake.Snake(((0, 0), (1, 0), (2, 0)))
    )

    try:
        result = input_board.move_player_up()
        assert 0 == 1
    except board.BoardPossitionError:
        assert 0 == 0


def test_board_move_player_up_2():
    input_board = board.Board(
                                nrows=3,
                                ncols=3,
                                player_possition=snake.Snake(((2, 0), (1, 0), (0, 0)))
    )

    try:
        result = input_board.move_player_up()
        assert 0 == 1
    except board.BoardPossitionError:
        assert 0 == 0


def test_board_move_player_up_3():
    input_board = board.Board(
                                nrows=5,
                                ncols=5,
                                player_possition=snake.Snake(((2, 2), (2, 3), (3, 3), (3, 4)))
    )

    output = board.Board(
                                nrows=5,
                                ncols=5,
                                player_possition=snake.Snake(((1, 2), (2, 2), (2, 3), (3, 3)))
    )

    result = input_board.move_player_up()

    assert result._player_possition == output._player_possition


def test_board_move_player_down_1():
    input_board = board.Board(
                                nrows=3,
                                ncols=3,
                                player_possition=snake.Snake(((2, 0), (1, 0), (0, 0)))
    )

    try:
        result = input_board.move_player_down()
        assert 0 == 1
    except board.BoardPossitionError:
        assert 0 == 0


def test_board_move_player_down_2():
    input_board = board.Board(
                                nrows=3,
                                ncols=3,
                                player_possition=snake.Snake(((0, 0), (1, 0), (2, 0)))
    )

    try:
        result = input_board.move_player_down()
        assert 0 == 1
    except board.BoardPossitionError:
        assert 0 == 0


def test_board_move_player_down_3():
    input_board = board.Board(
                                nrows=5,
                                ncols=5,
                                player_possition=snake.Snake(((2, 2), (2, 3), (3, 3), (3, 4)))
    )

    output = board.Board(
                                nrows=5,
                                ncols=5,
                                player_possition=snake.Snake(((3, 2), (2, 2), (2, 3), (3, 3)))
    )

    result = input_board.move_player_down()

    assert result._player_possition == output._player_possition


def test_board_move_player_left_1():
    input_board = board.Board(
                                nrows=3,
                                ncols=3,
                                player_possition=snake.Snake(((0, 0), (0, 1), (0, 2)))
    )

    try:
        result = input_board.move_player_left()
        assert 0 == 1
    except board.BoardPossitionError:
        assert 0 == 0


def test_board_move_player_left_2():
    input_board = board.Board(
                                nrows=3,
                                ncols=3,
                                player_possition=snake.Snake(((0, 2), (0, 1), (0, 0)))
    )

    try:
        result = input_board.move_player_left()
        assert 0 == 1
    except board.BoardPossitionError:
        assert 0 == 0


def test_board_move_player_left_3():
    input_board = board.Board(
                                nrows=5,
                                ncols=5,
                                player_possition=snake.Snake(((2, 2), (2, 3), (3, 3), (3, 4)))
    )

    output = board.Board(
                                nrows=5,
                                ncols=5,
                                player_possition=snake.Snake(((2, 1), (2, 2), (2, 3), (3, 3)))
    )

    result = input_board.move_player_left()

    assert result._player_possition == output._player_possition


def test_board_move_player_right_1():
    input_board = board.Board(
                                nrows=3,
                                ncols=3,
                                player_possition=snake.Snake(((0, 2), (0, 1), (0, 0)))
    )

    try:
        result = input_board.move_player_right()
        assert 0 == 1
    except board.BoardPossitionError:
        assert 0 == 0


def test_board_move_player_right_2():
    input_board = board.Board(
                                nrows=3,
                                ncols=3,
                                player_possition=snake.Snake(((0, 0), (0, 1), (0, 2)))
    )

    try:
        result = input_board.move_player_right()
        assert 0 == 1
    except board.BoardPossitionError:
        assert 0 == 0


def test_board_move_player_right_3():
    input_board = board.Board(
                                nrows=5,
                                ncols=5,
                                player_possition=snake.Snake(((2, 2), (2, 1), (3, 1), (3, 2)))
    )

    output = board.Board(
                                nrows=5,
                                ncols=5,
                                player_possition=snake.Snake(((2, 3), (2, 2), (2, 1), (3, 1)))
    )

    result = input_board.move_player_right()
