from crawler.domains.services import NotifyNewsService
from crawler.models import News


class TweetNewsService(NotifyNewsService):
    def notify(self, news: News) -> None:
        print(f"Tweet: {news.title}")
