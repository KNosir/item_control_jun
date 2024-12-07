from utils import connection_db
from logger import log_call
from utils import hash_maker


@log_call
def create_user_db(username, password):
    query = f'''INSERT INTO users(username,password)
        VALUES ('{username}','{hash_maker(password)}')'''
    try:
        connection_db(query)
        return True
    except:
        return False


@log_call
def set_new_pass(username, new_password):
    query = f'''
    update items
    set name = '{hash_maker(new_password)}'
    where name = '{username}'
    '''
    try:
        connection_db(query)
        return True
    except:
        return False


@log_call
def create_item(item_name: str, price: int) -> bool:
    slug = item_name.replace(' ', '_')
    query = f'''INSERT INTO items(name,slug,price,is_deleted)
        VALUES ('{item_name}','{slug}',{price},0)'''
    try:
        connection_db(query)
        return True
    except:
        return False


@log_call
def get_item_by_id(id: int) -> tuple:
    query = f'''select * from items where id={id} and is_deleted=0'''
    return connection_db(query)[0]


@log_call
def get_item_by_name(name: str) -> tuple | None:
    query = f'''select * from items where name='{name}'  '''
    return connection_db(query)


@log_call
def get_all_items() -> list:
    query = 'SELECT * FROM items where is_deleted=0'
    return connection_db(query)


@log_call
def get_all_item_sum() -> list:
    query = 'select sum(price) as amount from items where is_deleted=0'
    return connection_db(query)


@log_call
def change_item_name_by_name(old_name, new_name) -> bool:
    query = f'''
    update items
    set name = '{new_name}'
    where name = '{old_name}'
    '''
    try:
        connection_db(query)
        return True
    except:
        return False


@log_call
def change_item_price_by_name(item_name, new_price) -> bool:
    query = f'''
    update items
    set price = {new_price}
    where name = '{item_name}'
    '''
    try:
        connection_db(query)
        return True
    except:
        return False


@log_call
def delete_item_with_name(item_name) -> bool:
    query = f'''
    update items
    set is_deleted = 1
    where name = '{item_name}'
    '''
    try:
        connection_db(query)
        return True
    except:
        return False
