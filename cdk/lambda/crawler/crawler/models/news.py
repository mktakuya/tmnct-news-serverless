from dataclasses import dataclass
from datetime import date
from dataclasses_json import dataclass_json

from bs4 import BeautifulSoup

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
        return f"https://tmnct-news.m6a.jp/n/{self.slug}"

    def image_urls(self):
        soup = BeautifulSoup(self.content, "html.parser")
        return [img["src"] for img in soup.find_all("img")]
