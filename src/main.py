import sys
import time
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from src.spider import *
from src.writer import WriterFactory
from src.config import CLI

if __name__ == '__main__':
    CLI.init()
    writers = WriterFactory.generate()
    while True:
        for spider in [NBASpider, TencentSpider, HupuNBASpider, HupuInfoSpider]:
            news_collection = list(spider.run())
            [writer.write(news_collection) for writer in writers]
        time.sleep(1800)
