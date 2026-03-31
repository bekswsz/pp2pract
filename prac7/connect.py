import psycopg2
from config import params

def get_connection():
    try:
        conn = psycopg2.connect(**params)
        return conn
    except Exception as e:
        print(f"Ошибка подключения: {e}")
        return None