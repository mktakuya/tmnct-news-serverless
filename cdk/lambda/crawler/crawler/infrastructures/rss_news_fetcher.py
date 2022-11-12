import secrets

import feedparser

from crawler.domains import NewsFetcher
from crawler.models import News


def _parse_news(entry: dict) -> News:
    wp_pid = _extract_wp_pid(entry["guid"])
    slug = _generate_slug()

    return News(
        title=entry.title,
        wp_pid=wp_pid,
        url=entry.link,
        pub_date=entry.published,
        category=entry.category,
        content=entry.content[0].value,
        slug=slug,
    )


def _extract_wp_pid(url: str) -> int:
    return int(url.split("?p=")[1])


def _generate_slug() -> str:
    return secrets.token_hex(5)


class RssNewsFetcher(NewsFetcher):
    def __init__(self, feed_url: str):
        self.feed_url = feed_url

    def fetch(self) -> list[News]:
        feed = feedparser.parse(self.feed_url)

        return [_parse_news(entry) for entry in feed.entries]
