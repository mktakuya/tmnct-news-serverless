from ..models import News
from ..domains.news_repository import NewsRepository
from ..domains.news_fetcher import NewsFetcher
from ..domains.news_saver import NewsSaver


class NewsRepositoryImpl(NewsRepository):
    def __init__(self, fetcher: NewsFetcher, saver: NewsSaver):
        self.fetcher = fetcher
        self.saver = saver

    def fetch_latest_news(self) -> News:
        news = self.fetcher.fetch()

        return news[0]

    def is_exists(self, news: News) -> bool:
        return self.saver.is_exists(news)

    def save_news(self, news: News) -> None:
        self.saver.save(news)
