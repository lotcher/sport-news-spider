from abc import ABC, abstractmethod

from src.entity import News


class Sender(ABC):
    @classmethod
    @abstractmethod
    def send(cls, news: News):
        pass
