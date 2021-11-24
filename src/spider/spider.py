from abc import ABC, abstractmethod
from typing import List

import requests

from src.entity import News


class Spider(ABC):
    @classmethod
    def run(cls):
        return [cls.update_news(news) for news in cls.crawl_articles()]

    @classmethod
    @abstractmethod
    def crawl_articles(cls) -> List[News]:
        pass

    @classmethod
    def update_news(cls, news: News) -> News:
        return news

    @classmethod
    def send(cls, news: News):
        pass

    @classmethod
    def session(cls) -> requests.Session:
        session = requests.Session()
        session.headers.update({
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        })
        return session

    @classmethod
    def sleep(cls):
        import time
        time.sleep(1)
