from abc import ABC, abstractmethod

from ..models import News


class NewsSaver(ABC):
    @abstractmethod
    def save(self, news: News) -> None:
        pass
