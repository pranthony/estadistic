import os
from dotenv import load_dotenv

load_dotenv()

def get_supabase_config():
    return {
        'url': os.getenv('SUPABASE_URL'),
        'key': os.getenv('SUPABASE_KEY')
    }