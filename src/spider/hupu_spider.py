from typing import List

from .spider import Spider
from src.entity import News

from bools.log import Logger
from bools.functools import catch
from bools.datetime import Datetime
from lxml import etree
from tqdm import tqdm


class HupuSpider(Spider):
    @classmethod
    def crawl_articles(cls) -> List[News]:
        session = cls.session()
        for i in tqdm(range(1, 2), ncols=100):
            url = f'https://bbs.hupu.com/502-{i}'
            res = session.get(url)
            if res.status_code != 200:
                Logger.error(f'请求{url}失败，返回信息为：{res.text}')
            else:
                return catch(
                    lambda: [
                        News(title=msg.text, url=f'https://bbs.hupu.com{msg.get("href")}')
                        for msg in etree.HTML(res.text).xpath("//a[@class='p-title']")
                    ],
                    log=f'解析{res.text}失败，检查解析规则是否有错误',
                    except_return=[]
                )()
            cls.sleep()

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
