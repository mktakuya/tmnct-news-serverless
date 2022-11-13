from abc import ABC, abstractmethod

from ..models import News


class NewsSaver(ABC):
    @abstractmethod
    def save(self, news: News) -> None:
        pass

    # TODO: このメソッドの実装場所は要検討。そもそもNewsFetcher / NewsSaverは別に切り出さなくても良かったかも。
    def is_exists(self, news: News) -> bool:
        pass
