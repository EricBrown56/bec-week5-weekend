from db_connection import db_connection, Error

def return_book():
    '''Function to return a book to the library.'''
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
                if not availability:
                    query = "SELECT * FROM borrowed_books WHERE book_id = %s;"
                    cursor.execute(query, (book_id,))
                    borrowed_book = cursor.fetchall()
                    if borrowed_book:
                        query = "UPDATE borrowed_books SET return_date = CURRENT_TIMESTAMP WHERE book_id = %s;"
                        cursor.execute(query, (book_id,))
                        query = "UPDATE books SET availability = 1 WHERE id = %s;"
                        cursor.execute(query, (book_id,))
                        conn.commit() # commit the transaction
                        print(f"Book {title} returned successfully")
                    else:
                        print(f"Book {title} is not borrowed")
                else:
                    print(f"Book {title} is already available")
            else:
                print(f"Book with id {book_id} not found")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()