from os import system
from hashlib import sha256
import sqlite3
from logger import log_call


SALT = '_real_salt_'


@log_call
def hash_maker(text):
    text += SALT
    text = SALT + text
    text = text.encode()
    return sha256(text).hexdigest()


@log_call
def connection_db(query):
    conn = sqlite3.connect('files/data.db')
    cursor = conn.cursor()
    result = cursor.execute(query).fetchall()
    conn.commit()
    conn.close()
    return result

@log_call
def clean_console() -> None:
    system('cls')
