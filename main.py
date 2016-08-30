import sqlite3
import sys

conn = sqlite3.connect('movies.db')
print('Database Has Been Opened')

def display_main_menu():
    print('1) Search your Movies\n'
          '2) Edit an Entry\n'
          '3) Add a Movie Record\n'
          '4) Remove a Movie Record\n'
          '5) EXIT PROGRAM')

def main():

    print("Welcome to your movie catalog.")
    while True:
        display_main_menu()
        main_menu_choice = input('Please select an option from above.')
        if main_menu_choice == '1':
            print('Accessing Search Method')

        elif main_menu_choice == '2':
            print('Accessing Edit Method')

        elif main_menu_choice=='3':
            print('Accessing Add Method')

        elif main_menu_choice=='4':
            print('Accessing Remove Method')

        elif main_menu_choice=='5':
            sys.exit()

        else:
            print("That was not a valid Option.")





main()