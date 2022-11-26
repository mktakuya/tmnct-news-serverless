from abc import ABC, abstractmethod


class InputDataAdapter(ABC):
    @abstractmethod
    def transform(self, data):
        pass
