import sys

from Core.Application import Application
from Core.Library.App import Config

if __name__ == '__main__':
    Application(sys.argv).run()

    print(Config.get_conf('rabbitmq'))
