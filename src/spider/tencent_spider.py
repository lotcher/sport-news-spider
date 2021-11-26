import re
from typing import List

from lxml import etree
from bools.datetime import Datetime

from .spider import Spider
from ..entity import News


class TencentSpider(Spider):
    @classmethod
    def _crawl(cls, crawl_url: str) -> List[News]:
        res = cls.get('https://sports.qq.com/nba/')
        return [
            News(title=msg.text, url=msg.get("href"))
            for msg in etree.HTML(res.text).xpath('//div[@class="col-left"]//li/a')
        ]

    @classmethod
    def update_news(cls, news: News) -> News:
        res = cls.get(news.url)
        tree = etree.HTML(res.text)
        contents = tree.xpath('//div[@class="content-article"]/p[@class="one-p"]/text()')
        times = re.findall('pubtime\".*?\"(.*?)\"', res.text)
        img_urls = tree.xpath('//div[@class="content-article"]/p/img/@src')
        return News(
            news.title, news.url,
            timestamp=Datetime.from_str(times[0]).timestamp() if times else 0,
            content='\n'.join([p.strip() for p in contents if p.strip()]),
            img_urls=[f'https:{url}' for url in img_urls]
        )

    @classmethod
    def crawl_urls(cls) -> List[str]:
        return ['https://sports.qq.com/nba/']
