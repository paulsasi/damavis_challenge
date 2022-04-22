import logging
import logging.handlers


class Logger:

    class __Logger(logging.Logger):

        def __init__(self, name: str, path: str, level: int):
            super().__init__(name=name)

            stdout_handler = logging.StreamHandler()
            formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            stdout_handler.setFormatter(formatter)
            self.addHandler(stdout_handler)

            disk_handler = logging.handlers.RotatingFileHandler(path, maxBytes=10485760, backupCount=60)
            disk_handler.setFormatter(formatter)
            self.addHandler(disk_handler)

            self.setLevel(level=level)

    instance: __Logger = None

    def __new__(cls, name: str, path: str, level: int = logging.INFO):
        if not Logger.instance:
            Logger.instance = Logger.__Logger(name=name, path=path, level=level)
        return Logger.instance
