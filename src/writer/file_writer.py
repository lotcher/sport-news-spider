from os import path
from typing import Iterator

from .writer import Writer
from ..entity import News

BASE_DIR = path.dirname(path.dirname(path.dirname(path.abspath(__file__))))


class FileWriter(Writer):
    @classmethod
    def write(cls, news_collection: Iterator[News]):
        with open(f'{BASE_DIR}/sport-news.json', 'a') as f:
            f.write('\n'.join([news.to_json() for news in news_collection]))
