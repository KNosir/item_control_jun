from os import system
from hashlib import sha256
import sqlite3
from logger import log_call
import platform
from requests import get
from random import randint


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
    if platform.system() == 'Windows':
        system('cls')
    else:
        system('clear')


@log_call
def press_key() -> None:
    input('\n\nPress any key to continue......')
    return None


@log_call
def genarate_otp() -> int:
    random_num = randint(100000, 999999)
    return random_num


@log_call
def get_update_bot() -> list:
    try:
        updates = get(
            f'http://api.telegram.org/bot7686727377:AAEFMLpNv_eNDDJtO2Xbgrs5GsZU4aHtV2Q/getUpdates')
        return updates.json()['result']
    except:
        return []


@log_call
def remove_update_bot():
    updates = get_update_bot()
    if len(updates) > 0:
        max_update_id = 0
        for k in updates:
            max_update_id = max(max_update_id, k['update_id'])
        try:
            get(
                f'http://api.telegram.org/bot7686727377:AAEFMLpNv_eNDDJtO2Xbgrs5GsZU4aHtV2Q/getUpdates?offset={max_update_id+1}')
            return True
        except:
            return False
    else:
        return False


@log_call
def check_word_in_update(word) -> bool:
    update = get_update_bot()
    if len(update) > 0:
        for k in update:
            if str(word) in str(k['message']['text']):
                return True
    return False
