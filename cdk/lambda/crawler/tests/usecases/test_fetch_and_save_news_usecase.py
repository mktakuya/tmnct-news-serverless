import unittest
from datetime import datetime

from crawler.models import News
from crawler.domains import NewsRepository

from crawler.usecases import fetch_and_save_news_usecase


def _build_news() -> News:
    return News(
        title="サンプルニュース",
        wp_pid=1,
        url=f"https://www.tomakomai-ct.ac.jp/news/1.html",
        pub_date=datetime(2022, 1, 1),
        category="news",
        content="サンプルニュースの内容",
        slug="slug",
    )


class MockedNewsRepository(NewsRepository):
    def __init__(self, latest_news: News | None):
        self.latest_news = latest_news

    def fetch_latest_news(self):
        return _build_news()

    def is_exists(self, news):
        return self.latest_news is not None

    def save_news(self, news):
        return None


class TestFetchAndSaveNewsUsecase(unittest.TestCase):

    def test_fetch_and_save_news_usecase_when_latest_news_is_new(self):
        """
        最新ニュースが未保存の場合
        """
        news = _build_news()
        news_repository = MockedNewsRepository(latest_news=None)

        result = fetch_and_save_news_usecase.fetch_and_save_news(news_repository=news_repository)
        assert isinstance(result, News)
        assert result.wp_pid == 1

    def test_fetch_and_save_news_usecase_when_latest_news_is_not_new(self):
        news_repository = MockedNewsRepository(latest_news=_build_news())

        result = fetch_and_save_news_usecase.fetch_and_save_news(news_repository=news_repository)

        assert result is None
