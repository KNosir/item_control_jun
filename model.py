
import sqlite3


query_for_users = '''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT UNIQUE NOT NULL,
    password TEXT NOT NULL
)
'''


query_for_items = '''
CREATE TABLE IF NOT EXISTS items (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT UNIQUE NOT NULL,
    slug TEXT NOT NULL,
    price BIGINT NOT NULL
)
'''


def create_table(query: str) -> None:
    conn = sqlite3.connect('database/data.db')
    cursor = conn.cursor()
    try:
        cursor.execute(query)
    except:
        pass
    return None


create_table(query_for_users)
create_table(query_for_items)
