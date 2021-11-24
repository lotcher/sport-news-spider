from typing import List

from .spider import Spider
from src.entity import News

from bools.functools import catch
from bools.datetime import Datetime
from lxml import etree


class HupuSpider(Spider):
    @classmethod
    def crawl_urls(cls) -> List[str]:
        return [f'https://bbs.hupu.com/502-{i}' for i in range(1, 2)]

    @classmethod
    def crawl(cls, crawl_url: str) -> List[News]:
        res = cls.get(crawl_url)
        return catch(
            lambda: [
                News(title=msg.text, url=f'https://bbs.hupu.com{msg.get("href")}')
                for msg in etree.HTML(res.text).xpath("//a[@class='p-title']")
            ],
            log=f'解析【{res.text}】失败，检查网页是否正常返回或解析规则是否有错误',
            except_return=[]
        )()

    @classmethod
    def update_news(cls, news: News) -> News:
        article = cls.session().get(news.url).text
        tree = etree.HTML(article)
        contents = tree.xpath('//div[@class="thread-content-detail"]//p[@data-type="normal"]/text()')
        times = tree.xpath('//span[@class="post-user-comp-info-top-time"]/text()')
        img_urls = [
            url for url in tree.xpath('//div[@class="thread-content-detail"]//img/@src')
            if 'hupuapp/kanqiu' in url
        ]
        return News(
            news.title, news.url,
            timestamp=Datetime.from_str(times[0]).timestamp() if times else 0,
            content='\n'.join(contents), img_urls=img_urls
        )
