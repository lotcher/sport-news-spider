from typing import Iterator
from abc import ABC, abstractmethod

from bools.log import Logger

from src.entity import News


class Writer(ABC):
    def write(self, news_collection: Iterator[News]):
        Logger.info(f'通过{self}写入数据中...')
        self._write(news_collection)
        Logger.info(f'通过{self}写入数据完成')

    @abstractmethod
    def _write(self, news_collection: Iterator[News]):
        pass
