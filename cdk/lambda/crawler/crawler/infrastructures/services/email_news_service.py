from crawler.domains.services import NotifyNewsService
from crawler.models import News


class EmailNewsService(NotifyNewsService):
    def notify(self, news: News) -> None:
        print(f"Email: {news.title}")
