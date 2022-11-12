from crawler.domains.news_repository import NewsRepository
from crawler.models import News


def fetch_and_save_news(news_repository: NewsRepository) -> News | None:
    latest_news = news_repository.fetch_latest_news()

    if latest_news is None:
        return

    if news_repository.is_exists(latest_news):
        return

    news_repository.save_news(latest_news)

    return latest_news
