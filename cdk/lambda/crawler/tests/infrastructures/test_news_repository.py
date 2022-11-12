import unittest
import secrets
import random
from datetime import datetime, timedelta
from typing import get_args

from crawler.models import News, NewsCategory
from crawler.domains.news_fetcher import NewsFetcher
from crawler.domains.news_saver import NewsSaver
from crawler.infrastructures.news_repository import NewsRepositoryImpl


def _generate_slug() -> str:
    return secrets.token_hex(5)


def _build_news(sequence: int) -> News:
    categories = list(get_args(NewsCategory))
    category = random.choice(categories)

    return News(
        title=f"ニュース ${sequence}",
        wp_pid=1000 + sequence,
        url=f"https://www.tomakomai-ct.ac.jp/${category}/${sequence}.html",
        pub_date=datetime(2022, 1, 1) + timedelta(days=sequence - 1),
        category=category,
        content=f"ニュース ${sequence} の内容",
        slug=_generate_slug(),
    )


class MockedNewsFetcher(NewsFetcher):
    def fetch(self) -> list[News]:
        return [
            _build_news(sequence=3),
            _build_news(sequence=2),
            _build_news(sequence=1),
        ]


class MockedNewsSaver(NewsSaver):
    def is_exists(self, news: News) -> bool:
        return False

    def save(self, news: News) -> None:
        pass


mocked_fetcher = MockedNewsFetcher()
mocked_saver = MockedNewsSaver()


class TestNewsRepository(unittest.TestCase):
    def test_fetch_latest_news(self):
        repository = NewsRepositoryImpl(fetcher=mocked_fetcher, saver=mocked_saver)
        latest_news = repository.fetch_latest_news()

        # 単一のニュースが取得できていること
        assert isinstance(latest_news, News)

        # 最新のニュースが取得できていること
        assert latest_news.wp_pid == 1003

    def test_is_exists(self):
        repository = NewsRepositoryImpl(fetcher=mocked_fetcher, saver=mocked_saver)
        news = _build_news(sequence=1)
        assert repository.is_exists(news=news) is False


    def test_save_news(self):
        repository = NewsRepositoryImpl(fetcher=mocked_fetcher, saver=mocked_saver)

        news = _build_news(sequence=4)

        # ニュースが保存できていること
        assert repository.save_news(news) is None
