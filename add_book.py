from db_connection import db_connection, Error

def add_book():
    '''Function to add a book to the database.'''
    conn = db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            title = input("Enter the title of the book you would like to add: ").capitalize()
            new_book = (title,) # tuple
            query = "INSERT INTO books (title) VALUES (%s);"
            cursor.execute(query, new_book)
            conn.commit() # commit the transaction
            print(f"New book {title} added successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

