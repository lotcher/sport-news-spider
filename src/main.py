import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from spider import HupuInfoSpider, HupuNBASpider

if __name__ == '__main__':
    for spider in [HupuNBASpider, HupuInfoSpider]:
        print(list(spider.run()))
