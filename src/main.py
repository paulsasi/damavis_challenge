import os
import sys

sys.path.insert(0, str(os.getcwd()))

import os.path as path
import javaproperties
import json

import src.config.config as config
import src.logger.logger as logger
import src.core.validator as validator
import src.core.board as board
import src.core.snake as snake
import src.core.player as player
import src.core.path_calculator as path_calculator


def main(configs: config.Config) -> int:

    logging_service = logger.Logger(name='event-rule-frequency-logger', path=configs.get("logging.path"),
                                        level=configs.get("logging.level"))

    logging_service.info("============== SNAKE BOARD GAME DEPTH POSSIBILITIES CALCULATOR LAUNCH ==============")

    try:
        logging_service.info("Step1: Parse input arguments from configuration file.")
        input_args_board = validator.validate_board(configs.get("input.board"))
        input_args_depth = validator.validate_depth(configs.get("input.depth"))
        input_args_snake = validator.validate_snake(configs.get("input.snake"))

        logging_service.info("Step2: Initialize board and snake with starting configuration")
        snake_starting_position = snake.Snake(input_args_snake)
        board_starting_position = board.Board(nrows=input_args_board[0], ncols=input_args_board[1], player_possition=snake_starting_position)

        logging_service.info("Step3: Calculate the number of available different paths for the snake")
        number_of_available_paths = path_calculator.available_paths(initial_board=board_starting_position, depth=input_args_depth)

        logging_service.info(f"====> Number of valid paths of length {input_args_depth} the snake can make on the board: {number_of_available_paths}")
        logging_service.info("==================== ====================== =================== ====================")

        return number_of_available_paths

    except (validator.ValidationError, player.PlayerConstraintsError, board.BoardPossitionError) as e:
        logging_service.error(e)
        logging_service.info("============== EXECUTION ABORTED ==============")


if __name__ == '__main__':

    application_properties_path = path.dirname(path.dirname(path.abspath(__file__))) + '/application.properties'

    with open(application_properties_path, 'r') as f:
        application_properties = javaproperties.load(f)

    configs = config.Config(d=application_properties)

    main(configs)
