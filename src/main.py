import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from src.spider import HupuInfoSpider, HupuNBASpider
from src.sender import KafkaSender

if __name__ == '__main__':
    for spider in [HupuNBASpider, HupuInfoSpider]:
        [
            KafkaSender.send(news)
            for news in spider.run()
        ]
