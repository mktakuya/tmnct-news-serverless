from crawler.domains.news_repository import NewsRepository
from crawler.models import FetchAndSaveNewsResult


def fetch_and_save_news(news_repository: NewsRepository) -> FetchAndSaveNewsResult:
    latest_news = news_repository.fetch_latest_news()

    if news_repository.is_exists(latest_news):
        return FetchAndSaveNewsResult(
            updated=False,
            news=latest_news,
        )

    news_repository.save_news(latest_news)

    return FetchAndSaveNewsResult(
        updated=True,
        news=latest_news,
    )
