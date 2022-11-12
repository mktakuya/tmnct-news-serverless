from abc import ABC, abstractmethod

from ..models import News


class NewsFetcher(ABC):
    @abstractmethod
    def fetch(self) -> list[News]:
        pass
