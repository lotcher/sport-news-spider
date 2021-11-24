from abc import ABC
from typing import List

from .spider import Spider
from src.entity import News

from bools.datetime import Datetime
from lxml import etree


class HupuSpider(Spider, ABC):
    @classmethod
    def update_news(cls, news: News) -> News:
        article = cls.session().get(news.url).text
        tree = etree.HTML(article)
        contents = tree.xpath('//div[@class="main-post-info"]//div[@class="thread-content-detail"]//text()')
        times = tree.xpath('//span[@class="post-user-comp-info-top-time"]/text()')
        img_urls = tree.xpath('//div[@class="main-post-info"]//div[@class="thread-content-detail"]//img/@src')
        return News(
            news.title, news.url,
            timestamp=Datetime.from_str(times[0]).timestamp() if times else 0,
            content='\n'.join([p.strip() for p in contents if p.strip()]), img_urls=img_urls
        )


class HupuInfoSpider(HupuSpider):
    """[虎扑资讯](https://bbs.hupu.com/502-1)"""

    @classmethod
    def crawl_urls(cls) -> List[str]:
        return [f'https://bbs.hupu.com/502-{i}' for i in range(1, 2)]

    @classmethod
    def _crawl(cls, crawl_url: str) -> List[News]:
        res = cls.get(crawl_url)
        return [
            News(title=msg.text, url=f'https://bbs.hupu.com{msg.get("href")}')
            for msg in etree.HTML(res.text).xpath("//a[@class='p-title']")
        ]


class HupuNBASpider(HupuSpider):
    """[虎扑NBA](https://m.hupu.com/nba/news/1"""

    @classmethod
    def crawl_urls(cls) -> List[str]:
        return [f'https://m.hupu.com/nba/news/{i}' for i in range(1, 2)]

    @classmethod
    def _crawl(cls, crawl_url: str) -> List[News]:
        res = cls.get(crawl_url)
        return [
            News(title=''.join(item.xpath('div/div/h3/text()')),
                 url=f'https://bbs.hupu.com/{item.get("href").split("/")[-1]}')
            for item in etree.HTML(res.text).xpath("//a[@class='news-link']")
        ]
