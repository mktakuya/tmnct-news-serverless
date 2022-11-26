from abc import ABC, abstractmethod

from crawler.models import News


class NotifyNewsService(ABC):
    @abstractmethod
    def notify(self, news: News) -> None:
        pass
