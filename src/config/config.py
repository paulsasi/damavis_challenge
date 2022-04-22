from typing import Dict


class Config:

    class __Config:

        def __init__(self, d: Dict):
            self.__conf = d

        def get(self, name: str):
            return self.__conf.get(name)

    instance: __Config = None

    def __new__(cls, d: Dict):
        if not Config.instance:
            Config.instance = Config.__Config(d=d)
        return Config.instance
