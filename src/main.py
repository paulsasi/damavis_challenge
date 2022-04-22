import os
import sys

sys.path.insert(0, str(os.getcwd()))

import os.path as path
import javaproperties

import src.config.config as config


def main(configs: config.Config):
    print('main')


if __name__ == '__main__':

    application_properties_path = path.dirname(path.dirname(path.abspath(__file__))) + '/application.properties'

    with open(application_properties_path, 'r') as f:
        application_properties = javaproperties.load(f)

    configs = config.Config(d=application_properties)

    main(configs)
