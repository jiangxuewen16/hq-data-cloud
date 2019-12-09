import os
from enum import Enum

from Core.Helper.Helper import get_file_from_dir, parseYaml


class Env(Enum):
    PRODUCTION = 'production'
    DEVELOP = 'develop'

    @classmethod
    def has_env(cls, env_str: str) -> bool:
        if env_str not in cls.__members__:
            return False
        return True


class Config(object):
    _config_base_path: str = './Config/'
    _config_ext: list = ['yaml']

    conf: dict = {}

    def __init__(self, env: str):
        config_path = self._config_base_path + env
        files = get_file_from_dir(config_path, self._config_ext)
        for file in files:
            filepath, filename = os.path.split(file)
            shot_name, ext_name = os.path.splitext(filename)
            self.conf[shot_name] = parseYaml(file)

    @classmethod
    def get_conf(cls, conf_name: str):
        if conf_name not in cls.conf:
            raise Exception("配置名不存在!")
        return cls.conf[conf_name]
