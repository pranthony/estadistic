from typing import Dict, Any
from ..client import DatabaseClient
from ..factory import DatabaseClientFactory
from config import get_supabase_config

class SupabaseClient(DatabaseClient):
    def __init__(self, config: Dict[str, str]):
        self.url = config['url']
        self.key = config['key']
        self.client = None

    def connect(self) -> None:
        from supabase import create_client
        self.client = create_client(self.url, self.key)
        print("Conectado a Supabase")

    def query(self, query: str) -> Any:
        if not self.client:
            raise RuntimeError("No se ha establecido la conexión con Supabase")
        return self.client.table(query).select("*").execute()

class SupabaseClientFactory(DatabaseClientFactory):
    def create_client(self) -> SupabaseClient:
        config = get_supabase_config()
        return SupabaseClient(config)