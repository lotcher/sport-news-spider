from typing import Iterator
from .writer import Writer
from ..entity import News

from kafka import KafkaProducer


class KafkaWriter(Writer):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    @classmethod
    def write(cls, news_collection: Iterator[News]):
        for news in news_collection:
            cls.producer.send(topic='sport-news', value=news.to_json().encode('utf-8'))
