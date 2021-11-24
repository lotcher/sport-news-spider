import sys
from os import path

sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))

from spider import HupuSpider

if __name__ == '__main__':
    newsCollection = HupuSpider.run()
    print(list(newsCollection))
