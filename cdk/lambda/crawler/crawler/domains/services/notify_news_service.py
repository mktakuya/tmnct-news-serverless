from abc import ABC, abstractmethod


class NotifyNewsService(ABC):
    def __init__(self, news):
        self.news = news

    @abstractmethod
    def notify(self) -> None:
        pass
