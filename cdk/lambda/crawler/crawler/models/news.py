from dataclasses import dataclass
from datetime import datetime

from .news_category import NewsCategory


@dataclass
class News:
    title: str
    wp_pid: int
    url: str
    pub_date: datetime
    category: NewsCategory
    content: str
    slug: str
