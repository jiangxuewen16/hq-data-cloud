import os

from Core.Library.App import Env, Config


class Application(object):

    def __init__(self, argv: list):
        env = os.getenv('APP_ENV')
        self._app_env = env.lower() if Env.has_env(env) else Env.DEVELOP.value

    def run(self):
        Config(self._app_env)

    @property
    def app_env(self):
        return self._app_env
