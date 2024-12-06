from logger import log_call
from auth import *
from utils import *
from time import sleep
from crud import *
from prettytable import PrettyTable


@log_call
def login(command) -> bool:
    if command.isdigit() and int(command) == 1 or command.lower() == 'login':
        username = input('Please enter your username: ')
        if get_user(username) is None:
            print('Username not found create it')
            input('Enter any key to continue ')
            clean_console()
        password = input('Please enter your password: ')

        if get_access(username, password):
            return True
        else:
            False


@log_call
def main():
    while True:
        print('''1.Login \n2.Create username\n3.Forget password ''')
        command = input("Your command(use integer or text): ")
        if login(command):
            clean_console()
            sleep(1)
            # clean_console()
            break

    # if it is logged no need to get access twice
    while True:
        print('''\n1.Create item \n2.List all items\n3.Update item\n4.Delete item ''')
        command = input("Your command(use integer or text): ")

        # part 1.1 create
        if command.isdigit() and int(command) == 1 or command.lower().split(' ')[0] == 'create':
            item_name = input('Please enter item name: ')
            item_get_once = get_item_by_name(item_name)
            while len(item_get_once) != 0:
                item_name = input(
                    'Please enter item name which is not exist: ')
                item_get_once = get_item_by_name(item_name)

            item_price = input('Please enter item price: ')
            while True:
                try:
                    item_price = float(item_price)
                    break
                except:
                    pass
                item_price = input(
                    'Please enter item price correctly only float or integer number: ')

            if create_item(item_name, item_price):
                item_get = get_item_by_name(item_name)[0]
                clean_console()
                print(
                    f'Item created successfully: \nid:{item_get[0]}\nname:{item_get[1]}\nslug:{item_get[2]}\nprice:{item_get[3]}')
                press_key()
                clean_console()

    # part 1.2 list items
        if command.isdigit() and int(command) == 2 or command.lower().split(' ')[0] == 'list':
            table = PrettyTable()
            table.field_names = ['id', 'name', 'slug', 'price', 'is_deleted']

            for k in get_all_items():
                table.add_row(list(k))
            print(table)
            print('------Total------')
            print('       ', get_all_item_sum()[0][0])
            press_key()
            clean_console()

    # part 1.3 update item
        if command.isdigit() and int(command) == 3 or command.lower().split(' ')[0] == 'update':
            clean_console()
            print('''\nChange\n1.Name\n2.Price''')
            update_command = input('Your command(use integer): ')
            while update_command not in ['1', '2']:
                update_command = input(
                    'Enter command(use integer) correctly: ')

     # part 1.3.1 change name
            if update_command == '1':
                update_item_name = input('Enter item name: ')
                get_item_by_name_once = get_item_by_name(update_item_name)
                while len(get_item_by_name_once) == 0:
                    update_item_name = input('Enter item name correctly: ')
                    get_item_by_name_once = get_item_by_name(update_item_name)

                new_name = input('Enter new name for item: ')
                get_item_by_name_once = get_item_by_name(new_name)
                while len(get_item_by_name(new_name)) != 0:
                    new_name = 'Please enter name which is not exist: '
                    get_item_by_name_once = get_item_by_name(new_name)

                if change_item_name_by_name(update_item_name, new_name):
                    clean_console()
                    print('\n\nDone successfully')
                    press_key()
                    clean_console()

    # part 1.3.2 change price by name
            if update_command == '2':
                update_item_name = input('Enter item name: ')
                get_item_by_name_once = get_item_by_name(update_item_name)
                while len(get_item_by_name_once) == 0:
                    update_item_name = input('Enter item name correctly: ')
                    get_item_by_name_once = get_item_by_name(update_item_name)

                item_price = input('Please enter item price: ')
                while True:
                    try:
                        item_price = float(item_price)
                        break
                    except:
                        pass
                    item_price = input(
                        'Please enter item price correctly only float or integer number: ')

                if change_item_price_by_name(update_item_name, item_price):
                    clean_console()
                    print('\n\nDone successfully')
                    press_key()
                    clean_console()
        # part 1.4 Delete item by name
        if command.isdigit() and int(command) == 4 or command.lower().split(' ')[0] == 'delete':
            update_item_name = input('Enter item name: ')
            get_item_by_name_once = get_item_by_name(update_item_name)
            while len(get_item_by_name_once) == 0:
                update_item_name = input('Enter item name correctly: ')
                get_item_by_name_once = get_item_by_name(update_item_name)

            if delete_item_with_name(update_item_name):
                clean_console()
                print('\n\nDone successfully')
                press_key()
                clean_console()


if __name__ == '__main__':
    main()
