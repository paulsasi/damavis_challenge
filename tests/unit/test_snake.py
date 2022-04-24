import src.core.snake as snake
import src.core.player as player


def test_snake_init_1():
    input_snake = ((0, 0), (1, 1), (2, 2))

    try:
        selected_snake = snake.Snake(input_snake)
        assert 0 == 1
    except player.PlayerConstraintsError:
        assert 0 == 0


def test_snake_init_2():
    input_snake = ((0, 0), (0, 1), (2, 2))

    try:
        selected_snake = snake.Snake(input_snake)
        assert 0 == 1
    except player.PlayerConstraintsError:
        assert 0 == 0


def test_snake_init_3():
    input_snake = ((0, 0), (0, 1), (0, 3))

    try:
        selected_snake = snake.Snake(input_snake)
        assert 0 == 1
    except player.PlayerConstraintsError:
        assert 0 == 0


def test_snake_init_4():
    input_snake = ((0, 0), (0, 1), (0, 2))

    output_head = (0, 0)
    output_snake = ((0, 0), (0, 1), (0, 2))

    result_snake = snake.Snake(input_snake)

    assert result_snake.head == output_head and result_snake.snake == output_snake


def test_snake_init_5():
    input_snake = ((0, 0), (0, 1), (1, 1), (2, 1))

    output_head = (0, 0)
    output_snake = ((0, 0), (0, 1), (1, 1), (2, 1))

    result_snake = snake.Snake(input_snake)

    assert result_snake.head == output_head and result_snake.snake == output_snake


def test_snake_init_6():
    input_snake = ((0, 0), (0, 1), (0, 0))

    try:
        selected_snake = snake.Snake(input_snake)
        assert 0 == 1
    except player.PlayerConstraintsError:
        assert 0 == 0


def test_snake_is_within_limits_1():
    input_snake = snake.Snake(((2, 0), (3, 0), (4, 0)))
    input_rows, input_cols = 5, 5

    assert input_snake.is_within_limits(input_rows, input_cols) is True


def test_snake_is_within_limits_2():
    input_snake = snake.Snake(((-1, 0), (0, 0), (1, 0)))
    input_rows, input_cols = 5, 5

    assert input_snake.is_within_limits(input_rows, input_cols) is False


def test_snake_is_within_limits_3():
    input_snake = snake.Snake(((0, 0), (0, 1), (0, 2), (0, 3)))
    input_rows, input_cols = 3, 3

    assert input_snake.is_within_limits(input_rows, input_cols) is False


def test_snake_is_within_limits_4():
    input_snake = snake.Snake(((0, 0), (1, 0), (2, 0), (3, 0)))
    input_rows, input_cols = 3, 5

    assert input_snake.is_within_limits(input_rows, input_cols) is False


def test_snake_move_up_1():
    input_snake = snake.Snake(((2, 0), (3, 0), (4, 0)))
    output = snake.Snake(((1, 0), (2, 0), (3, 0)))

    result = input_snake.move_up()
    assert result.head == output.head and result.snake == output.snake


def test_snake_move_up_2():
    input_snake = snake.Snake(((3, 2), (4, 2), (4, 1), (3, 1), (3, 0)))
    output = snake.Snake(((2, 2), (3, 2), (4, 2), (4, 1), (3, 1)))

    result = input_snake.move_up()
    assert result.head == output.head and result.snake == output.snake


def test_snake_move_up_3():
    input_snake = snake.Snake(((2, 0), (1, 0), (0, 0)))
    try:
        result = input_snake.move_up()
        assert 0 == 1
    except player.PlayerConstraintsError:
        assert 0 == 0


def test_snake_move_down_1():
    input_snake = snake.Snake(((4, 0), (3, 0), (2, 0)))
    output = snake.Snake(((5, 0), (4, 0), (3, 0)))

    result = input_snake.move_down()
    assert result.head == output.head and result.snake == output.snake


def test_snake_move_down_2():
    input_snake = snake.Snake(((3, 0), (3, 1), (4, 1), (4, 2), (3, 2)))
    output = snake.Snake(((4, 0), (3, 0), (3, 1), (4, 1), (4, 2)))

    result = input_snake.move_down()
    assert result.head == output.head and result.snake == output.snake


def test_snake_move_down_3():
    input_snake = snake.Snake(((0, 0), (1, 0), (2, 0)))
    try:
        result = input_snake.move_down()
        assert 0 == 1
    except player.PlayerConstraintsError:
        assert 0 == 0


def test_snake_move_left_1():
    input_snake = snake.Snake(((1, 1), (1, 2), (1, 3)))
    output = snake.Snake(((1, 0), (1, 1), (1, 2)))

    result = input_snake.move_left()
    assert result.head == output.head and result.snake == output.snake


def test_snake_move_left_2():
    input_snake = snake.Snake(((3, 1), (3, 2), (4, 2), (4, 3), (3, 3)))
    output = snake.Snake(((3, 0), (3, 1), (3, 2), (4, 2), (4, 3)))

    result = input_snake.move_left()
    assert result.head == output.head and result.snake == output.snake


def test_snake_move_left_3():
    input_snake = snake.Snake(((0, 2), (0, 1), (0, 0)))
    try:
        result = input_snake.move_left()
        assert 0 == 1
    except player.PlayerConstraintsError:
        assert 0 == 0


def test_snake_move_right_1():
    input_snake = snake.Snake(((1, 3), (1, 2), (1, 1)))
    output = snake.Snake(((1, 4), (1, 3), (1, 2)))

    result = input_snake.move_right()
    assert result.head == output.head and result.snake == output.snake


def test_snake_move_right_2():
    input_snake = snake.Snake(((3, 3), (4, 3), (4, 2), (3, 2), (3, 1)))
    output = snake.Snake(((3, 4), (3, 3), (4, 3), (4, 2), (3, 2)))

    result = input_snake.move_right()
    assert result.head == output.head and result.snake == output.snake


def test_snake_move_right_3():
    input_snake = snake.Snake(((0, 0), (0, 1), (0, 2)))
    try:
        result = input_snake.move_right()
        assert 0 == 1
    except player.PlayerConstraintsError:
        assert 0 == 0
