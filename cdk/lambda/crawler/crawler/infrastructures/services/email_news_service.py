from crawler.domains.services import NotifyNewsService


class EmailNewsService(NotifyNewsService):
    def notify(self) -> None:
        print(f"Email: {self.news.title}")
