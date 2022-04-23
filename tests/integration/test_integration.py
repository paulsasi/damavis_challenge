from tkinter import N
import src.config.config as config
import src.main as main


def test_integration_1():

    configs = config.Config({
        "input.board": "[4,3]",
        "input.depth": "3",
        "input.snake": "[[2, 2], [3, 2], [3, 1], [3, 0], [2, 0], [1, 0], [0, 0]]",
        "logging.path": "./board_snake_depth_calculator.log",
        "logging.level": "CRITICAL"
    })

    assert main.main(configs) == 7


def test_integration_2():
    config.Config.instance = None  # Hack to avoid Config singleton pattern while testing
    configs = config.Config({
        "input.board": "[2,3]",
        "input.depth": "10",
        "input.snake": "[[0, 2], [0, 1], [0, 0], [1, 0], [1, 1], [1, 2]]",
        "logging.path": "./board_snake_depth_calculator.log",
        "logging.level": "CRITICAL"
    })

    assert main.main(configs) == 1


def test_integration_3():
    config.Config.instance = None
    configs = config.Config({
        "input.board": "[10,10]",
        "input.depth": "4",
        "input.snake": "[[5, 5], [5, 4], [4, 4], [4, 5]]",
        "logging.path": "./board_snake_depth_calculator.log",
        "logging.level": "CRITICAL"
    })

    assert main.main(configs) == 81
