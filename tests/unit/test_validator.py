import src.core.validator as validator


def test_validate_board_1():
    input_board = ""
    try:
        output = validator.validate_board(input_board)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_board_2():
    input_board = "test"
    try:
        output = validator.validate_board(input_board)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_board_3():
    input_board = "[5,"
    try:
        output = validator.validate_board(input_board)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_board_4():
    input_board = "[5, 5, 5]"
    try:
        output = validator.validate_board(input_board)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_board_5():
    input_board = "[0, 5]"
    try:
        output = validator.validate_board(input_board)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_board_6():
    input_board = "[11, 5]"
    try:
        output = validator.validate_board(input_board)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_board_7():
    input_board = "[5, 0]"
    try:
        output = validator.validate_board(input_board)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_board_8():
    input_board = "[5, 11]"
    try:
        output = validator.validate_board(input_board)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_board_9():
    input_board = "[5.5, 11]"
    try:
        output = validator.validate_board(input_board)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_board_10():
    input_board = "[5, 7.7]"
    try:
        output = validator.validate_board(input_board)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_board_11():
    input_board = "[10, 5]"
    assert validator.validate_board(input_board) == (10, 5)


def test_validate_board_12():
    input_board = "[6, 10]"
    assert validator.validate_board(input_board) == (6, 10)


def test_validate_board_13():
    input_board = "[5, 7]"
    assert validator.validate_board(input_board) == (5, 7)


def test_validate_depth_1():
    input_depth = ""
    try:
        output = validator.validate_depth(input_depth)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_depth_2():
    input_depth = "test"
    try:
        output = validator.validate_depth(input_depth)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_depth_3():
    input_depth = "5.5"
    try:
        output = validator.validate_depth(input_depth)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_depth_4():
    input_depth = "0"
    try:
        output = validator.validate_depth(input_depth)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_depth_5():
    input_depth = "21"
    try:
        output = validator.validate_depth(input_depth)
        assert 0 == 1
    except validator.ValidationError:
        assert 0 == 0


def test_validate_depth_6():
    input_depth = "15"
    assert validator.validate_depth(input_depth) == 15


def test_validate_snake_1():
    input_snake = "[[2, 2], [3, ]]"
    try:
        output = validator.validate_snake(input_snake)
        assert 0 == 1
    except validator.ValidationError:
        assert 1 == 1


def test_validate_snake_2():
    input_snake = "[[2, 2, [3, 3]]"
    try:
        output = validator.validate_snake(input_snake)
        assert 0 == 1
    except validator.ValidationError:
        assert 1 == 1


def test_validate_snake_3():
    input_snake = "[2, 2, 5, 6]"
    try:
        output = validator.validate_snake(input_snake)
        assert 0 == 1
    except validator.ValidationError:
        assert 1 == 1


def test_validate_snake_4():
    input_snake = "[[2, 2], [3, 3]]"
    try:
        output = validator.validate_snake(input_snake)
        assert 0 == 1
    except validator.ValidationError:
        assert 1 == 1


def test_validate_snake_5():
    input_snake = "[[2, 2], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3], [3, 3]]"
    try:
        output = validator.validate_snake(input_snake)
        assert 0 == 1
    except validator.ValidationError:
        assert 1 == 1


def test_validate_snake_6():
    input_snake = "[[2, 2], [3, 3], [3, 3, 5], [3, 3]]"
    try:
        output = validator.validate_snake(input_snake)
        assert 0 == 1
    except validator.ValidationError:
        assert 1 == 1


def test_validate_snake_7():
    input_snake = "[[2, 2], [3, 3], [3, 3], [3, 3]]"
    output = ((2, 2), (3, 3), (3, 3), (3, 3))
    assert validator.validate_snake(input_snake) == output
