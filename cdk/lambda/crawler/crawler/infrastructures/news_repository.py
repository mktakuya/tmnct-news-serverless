from ..models import News
from ..domains.news_repository import NewsRepository
from ..domains.news_fetcher import NewsFetcher


class NewsRepositoryImpl(NewsRepository):
    def __init__(self, fetcher: NewsFetcher):
        self.fetcher = fetcher

    def fetch_latest_news(self) -> News:
        news = self.fetcher.fetch()

        return news[0]

    def save_news(self, news: News) -> None:
        pass
