from typing import Iterator
from dataclasses import dataclass

import pandas as pd

from .writer import Writer
from ..entity import News

from bools.dbc import ElasticSearch


@dataclass
class ESWriter(Writer):
    index: str = 'sport-news'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.es = ElasticSearch(base_url=kwargs.get('url', 'http://localhost:9200'), patch_pandas=True)

    def _write(self, news_collection: Iterator[News]):
        pd.DataFrame([news.__dict__ for news in news_collection]).to_es(index=self.index)
