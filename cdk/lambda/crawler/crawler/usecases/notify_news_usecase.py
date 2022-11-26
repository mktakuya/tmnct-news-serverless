from crawler.models import News
from crawler.domains.services.notify_news_service import NotifyNewsService


def notify_news(news: News, notifier: NotifyNewsService) -> None:
    notifier.notify(news)
