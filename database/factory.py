from abc import ABC, abstractmethod
from .client import DatabaseClient

class DatabaseClientFactory(ABC):
    @abstractmethod
    def create_client(self) -> DatabaseClient:
        pass