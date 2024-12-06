from utils import hash_maker, connection_db
from logger import log_call


@log_call
def get_user(user_name) -> tuple | None:
    if "'" in user_name:
        return None
    query = f'''
    select * from users where username='{user_name}'
    limit 1
    '''

    try:
        return connection_db(query)[0]
    except:
        return None


@log_call
def create_user(username, password) -> str | None:
    password_hash = hash_maker(password)
    query = f'''INSERT INTO users(username, password) 
        VALUES ('{username}','{password_hash}')'''
    try:
        return connection_db(query)
    except:
        return None


@log_call
def get_access(username, password) -> bool:
    if "'" in username or "'" in password:
        return False

    user = get_user(username)
    if user is None:
        return False

    if user[1] == username and user[2] == hash_maker(password):
        return True
    else:
        False
