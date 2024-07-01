from db_connection import db_connection, Error

def borrow_book():
    '''Function to borrow a book from the library.'''
    conn = db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            book_id = int(input("Enter the book id: "))
            query = "SELECT * FROM books WHERE id = %s;"
            cursor.execute(query, (book_id,))
            book = cursor.fetchall()
            if book:
                book_id, title, availability = book[0]
                if availability:
                    user_id = int(input("Enter the user id: "))
                    query = "SELECT * FROM users WHERE id = %s;"
                    cursor.execute(query, (user_id,))
                    user = cursor.fetchall()
                    if user:
                        user_id, email, name = user[0]
                        query = "INSERT INTO borrowed_books (book_id, user_id, borrow_date) VALUES (%s, %s, CURRENT_TIMESTAMP);"
                        cursor.execute(query, (book_id, user_id))
                        query = "UPDATE books SET availability = 0 WHERE id = %s;"
                        cursor.execute(query, (book_id,))
                        conn.commit() # commit the transaction
                        print(f"Book {title} borrowed successfully by {name}")
                    else:
                        print(f"User with id {user_id} not found")
                else:
                    print(f"Book {title} is not available")
            else:
                print(f"Book with id {book_id} not found")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()