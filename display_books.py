from db_connection import db_connection, Error

def fetch_books():
    '''Function to fetch all books from the library.'''
    conn = db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM books;"
            cursor.execute(query)
            for id, title, availability in cursor.fetchall():
                print(f"{id}: {title}, Available: {availability}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def fetch_book():
    '''Function to fetch a specific book from the library'''
    conn = db_connection()
    if conn is not None:
        try:
            book_id = input("Enter the book title you are looking for: ")
            cursor = conn.cursor()
            query = "SELECT * FROM books WHERE title = %s;"
            cursor.execute(query, (book_id,))
            id, title, availability  = cursor.fetchall()[0]
            print(f"{id}: {title}, Available: {availability}")
        except Error as e:
            print(f"Error: {e}")
        finally:
             if conn and conn.is_connected():
                cursor.close()
                conn.close()
if __name__ == "__main__":
    fetch_books()