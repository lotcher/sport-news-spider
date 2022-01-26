from abc import ABC, abstractmethod
from typing import List, Generator

import requests
from bools.log import Logger
from bools.functools import catch
from tqdm import tqdm

from src.entity import News


class Spider(ABC):
    source = ''

    @classmethod
    def run(cls) -> Generator[News, None, None]:
        for url in cls.crawl_urls():
            yield from [cls.update_news(news) for news in tqdm(cls.crawl(url), ncols=100)]
            cls.sleep()

    @classmethod
    def crawl(cls, crawl_url: str) -> List[News]:
        Logger.info(f'开始爬取[{crawl_url}]...')
        return catch(
            lambda: cls._crawl(crawl_url),
            log=f'解析【{crawl_url}】失败，检查网页是否正常返回或解析规则是否有错误',
            except_return=[]
        )()

    @classmethod
    @abstractmethod
    def _crawl(cls, crawl_url: str) -> List[News]:
        pass

    @classmethod
    def update_news(cls, news: News) -> News:
        return news

    @classmethod
    def session(cls) -> requests.Session:
        session = requests.Session()
        session.headers.update({
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36'
        })
        return session

    @classmethod
    def sleep(cls):
        import time
        time.sleep(1)

    @classmethod
    def get(cls, url) -> requests.Response:
        res = cls.session().get(url)
        if res.status_code != 200:
            Logger.error(f'请求{url}失败，返回信息为：{res.text}')
        else:
            return res

    @classmethod
    @abstractmethod
    def crawl_urls(cls) -> List[str]:
        pass
