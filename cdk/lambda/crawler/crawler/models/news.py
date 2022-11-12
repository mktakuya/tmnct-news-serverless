from dataclasses import dataclass
from datetime import datetime

from dataclasses_json import dataclass_json

from .news_category import NewsCategory


@dataclass_json
@dataclass
class News:
    title: str
    wp_pid: int
    url: str
    pub_date: datetime
    category: NewsCategory
    content: str
    slug: str
