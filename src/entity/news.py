from dataclasses import dataclass, field
from typing import List
from hashlib import md5

from bools.datetime import Datetime


@dataclass
class News:
    title: str
    url: str
    timestamp: int = 0
    content: str = ''
    img_urls: List[str] = field(default_factory=list)

    def __post_init__(self):
        self.id = md5(self.title.encode()).hexdigest()
        self.time = Datetime.fromtimestamp(self.timestamp)
