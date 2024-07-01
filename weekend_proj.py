import mysql.connector # importing mysql connector library that we pip installed as well as all of the other modules we will be using
from db_connection import db_connection, Error
from add_book import add_book
from display_books import fetch_books, fetch_book
from return_book import return_book
from user_add import add_user
from user_fetch import fetch_users, fetch_user
from borrow_book import borrow_book

def main():
    '''Main function that will display the main menu and allow the user to choose what they would like to do.'''
    print(''' Welcome to the Library Management System with Database Integration!
    ****
    Main Menu:
    1. Book Operations
    2. User Operations
    3. Quit''')
    while True:    
        try:
            choice = int(input("Please enter the number of what you would like to do from the Main Menu: "))
            if choice == 1:
                print('''Book Operations Menu:
                1. Add a Book
                2. Borrow a Book
                3. Return a Book
                4. Search for a Book
                5. Show all Books
                6. Main Menu
                ''')
                book_choice = int(input("Please enter the number of what you would like to do from Book choices: "))
                if book_choice == 1:
                     add_book()
                     main()
                elif book_choice == 2:
                     fetch_books()
                     borrow_book()
                     main()
                elif book_choice == 3:
                     fetch_books()
                     return_book()
                     main()
                elif book_choice == 4:
                     fetch_books()
                     fetch_book()
                     main()
                elif book_choice == 5:
                     fetch_books()
                     main()
                elif book_choice == 6:
                     main()
            elif choice == 2:
                print('''User Operations Menu:
                1. Register
                2. View Users
                3. Get User Info
                4. Main Menu
                ''')
                user_choice = int(input("Please enter the number of what you would like to do: "))
                if user_choice == 1:
                     add_user()
                     main()
                elif user_choice == 2:
                     fetch_users()
                     main()
                elif user_choice == 3:
                     fetch_users()
                     fetch_user()
                     main()
                elif user_choice == 4:
                     main()
            elif choice == 3:
                print('Thank you for using the Library Management System with Database Integration!')
            break
        except ValueError:
            print("Please enter a valid number")
            main()
        except Error as e:
            print(f"Error: {e}")
            return None
        

if __name__ == "__main__":
     main()