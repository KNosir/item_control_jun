from utils import connection_db
from logger import log_call


@log_call
def create_item(item_name: str, price: int) -> bool:
    slug = item_name.replace(' ', '_')
    query = f'''INSERT INTO items(name,slug,price) 
        VALUES ('{item_name}','{slug}',{price})'''
    try:
        connection_db(query)
        return True
    except:
        return False
