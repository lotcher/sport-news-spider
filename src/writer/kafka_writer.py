from typing import Iterator
from dataclasses import dataclass
from .writer import Writer
from ..entity import News

from kafka import KafkaProducer


@dataclass
class KafkaWriter(Writer):
    topic: str = 'sport-news'

    def __init__(self, **kwargs):
        self.producer = KafkaProducer(**{
            k: kwargs.get(k, default)
            for k, default in KafkaProducer.DEFAULT_CONFIG.items()
        })
        for k, v in kwargs.items():
            setattr(self, k, v)

    def _write(self, news_collection: Iterator[News]):
        for news in news_collection:
            self.producer.send(topic=self.topic, value=news.to_json().encode('utf-8'))
