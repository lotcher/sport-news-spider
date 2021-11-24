from typing import Iterator
from abc import ABC, abstractmethod

from src.entity import News


class Writer(ABC):
    @classmethod
    @abstractmethod
    def write(cls, news_collection: Iterator[News]):
        pass
