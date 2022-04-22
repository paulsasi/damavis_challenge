import src.validator as validator


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
    input_board = "[5, 7]"
    assert validator.validate_board(input_board) == (5, 7)
