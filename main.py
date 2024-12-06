from logger import log_call
from auth import *
from utils import *


@log_call
def login(command) -> bool:
    if command.isdigit() and int(command) == 1 or command.lower() == 'login':

        username = input('Please enter your username: ')
        if get_user(username) is None:
            clean_console()
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
            print('''1.Login \n2.Create username\n3.Forget password ''')


if __name__ == '__main__':
    main()
