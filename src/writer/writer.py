from typing import List
from abc import ABC, abstractmethod

from bools.log import Logger

from src.entity import News


class Writer(ABC):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def write(self, news_collection: List[News]):
        Logger.info(f'通过{self}写入数据中...')
        if len(news_collection) > 0:
            self._write(news_collection)
        Logger.info(f'通过{self}写入数据完成')

    @abstractmethod
    def _write(self, news_collection: List[News]):
        pass
