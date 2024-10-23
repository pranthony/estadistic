from typing import Dict
from .client import DatabaseClient
from .factory import DatabaseClientFactory
from .clients.supabase_client import SupabaseClientFactory

class DatabaseManager:
    _instance = None
    _clients: Dict[str, DatabaseClient] = {}

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(DatabaseManager, cls).__new__(cls)
        return cls._instance

    def get_client(self, client_type: str) -> DatabaseClient:
        if client_type not in self._clients:
            factory = self._get_factory(client_type)
            client = factory.create_client()
            client.connect()
            self._clients[client_type] = client
        return self._clients[client_type]

    def _get_factory(self, client_type: str) -> DatabaseClientFactory:
        factories = {
            'supabase': SupabaseClientFactory()
        }
        if client_type not in factories:
            raise ValueError(f"Tipo de cliente no soportado: {client_type}")
        return factories[client_type]