from abc import ABC, abstractmethod

from ..models import News


class NewsRepository(ABC):
    @abstractmethod
    def fetch_latest_news(self) -> News:
        pass

    @abstractmethod
    def save_news(self, news: News) -> None:
        pass
