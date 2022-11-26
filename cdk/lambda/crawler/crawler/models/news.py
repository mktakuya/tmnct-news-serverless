from dataclasses import dataclass
from datetime import date

from dataclasses_json import dataclass_json

from .news_category import NewsCategory


@dataclass_json
@dataclass
class News:
    title: str
    wp_pid: int
    url: str
    pub_date: date
    category: NewsCategory
    content: str
    slug: str

    def short_url(self):
        # TODO: 環境ごとの正しいURLで実装する
        return f"https://example.com/n/{self.slug}"
