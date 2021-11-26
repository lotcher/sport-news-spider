from typing import Iterator
from dataclasses import dataclass

from .writer import Writer
from src.entity import News
from src.config import BASE_DIR


@dataclass
class FileWriter(Writer):
    path: str = f'{BASE_DIR}/sport-news.json'

    def _write(self, news_collection: Iterator[News]):
        with open(self.path, 'a', encoding='utf-8') as f:
            f.write('\n'.join([news.to_json() for news in news_collection]) + '\n')
