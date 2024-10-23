from abc import ABC, abstractmethod
from typing import Any

class DatabaseClient(ABC):
    @abstractmethod
    def connect(self) -> None:
        pass

    @abstractmethod
    def query(self, query: str) -> Any:
        pass