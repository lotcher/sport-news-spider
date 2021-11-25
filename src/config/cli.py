from os import path

import argparse

from .config import Config

BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))

_CONFIG, _DEFAULT = 'config', f'{BASE_DIR}/config/default.yaml'


class CLI:
    @classmethod
    def parse(cls):
        parser = argparse.ArgumentParser(description='Spider命令行参数')
        parser.add_argument(
            '--config', '-f', dest=_CONFIG, required=False,
            help=f'加载的yaml配置文件路径, 默认为：{_DEFAULT}', default=_DEFAULT
        )
        return parser.parse_args()

    @classmethod
    def init(cls):
        args = CLI.parse()
        Config.from_yaml(getattr(args, _CONFIG))
