from crawler.domains.services.notify_news_service import NotifyNewsService


def notify_news(notifier: NotifyNewsService) -> None:
    notifier.notify()
