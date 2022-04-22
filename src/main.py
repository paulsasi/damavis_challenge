import os
import sys

sys.path.insert(0, str(os.getcwd()))

import os.path as path
import javaproperties
import json

import src.config.config as config
import src.logger.logger as logger
import src.validator as validator


def main(configs: config.Config):

    logging_service = logger.Logger(name='event-rule-frequency-logger', path=configs.get("logging.path"),
                                        level=configs.get("logging.level"))

    logging_service.info("============== SNAKE BOARD GAME DEPTH POSSIBILITIES CALCULATOR LAUNCH ==============")

    try:
        input_args_board = validator.validate_board(configs.get("input.depth"))
        input_args_depth = validator.validate_depth(configs.get("input.depth"))
        input_args_snake = validator.validate_snake(configs.get("input.snake"))

    except validator.ValidationError as e:
        logging_service.error(e)
        logging_service.info("============== EXECUTION ABORTED ==============")


if __name__ == '__main__':

    application_properties_path = path.dirname(path.dirname(path.abspath(__file__))) + '/application.properties'

    with open(application_properties_path, 'r') as f:
        application_properties = javaproperties.load(f)

    configs = config.Config(d=application_properties)

    main(configs)
