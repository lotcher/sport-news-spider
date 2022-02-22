from typing import List

from .spider import Spider
from ..entity import News


class NBASpider(Spider):
    source = 'NBA.COM'

    @classmethod
    def _crawl(cls, crawl_url: str) -> List[News]:
        res = cls.get(crawl_url).json()
        return [
            News(
                title=msg['title'], url=msg['permalink'], timestamp=int(msg['timestamp'] / 1000),
                contents=[msg['excerpt']], img_urls=[msg['featuredImage']]
            )
            for msg in res['results']['items']
        ]

    @classmethod
    def crawl_urls(cls) -> List[str]:
        return ['https://content-api-prod.nba.com/public/1/content?page=1&count=100&types=post&term-category=1633&region=international-no-nbatv']
