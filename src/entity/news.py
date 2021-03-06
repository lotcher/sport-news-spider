import json
from dataclasses import dataclass, field
from typing import List
from hashlib import md5

from bools.datetime import Datetime


@dataclass
class News:
    title: str
    url: str
    timestamp: int = 0
    contents: List[str] = field(default_factory=list)
    img_urls: List[str] = field(default_factory=list)
    source: str = ''

    def __post_init__(self):
        self.id = md5(self.url.encode()).hexdigest()
        self.timestamp = int(self.timestamp * 1000)
        self.time = Datetime.fromtimestamp(self.timestamp, precision='ms').str

    def to_json(self):
        return json.dumps(self.__dict__, ensure_ascii=False)
