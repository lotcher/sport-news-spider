from .sender import Sender
from ..entity import News

from kafka import KafkaProducer


class KafkaSender(Sender):
    producer = KafkaProducer(bootstrap_servers='localhost:9092')

    @classmethod
    def send(cls, news: News):
        cls.producer.send(topic='sport-news', value=news.to_json().encode('utf-8'))
