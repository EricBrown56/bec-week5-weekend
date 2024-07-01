from db_connection import db_connection, Error

def add_user():
    '''Function to add a user to the database.'''
    conn = db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            name = input("What is your name? ").title()
            email = input("What is your email? ")
            new_customer = (name, email) # tuple
            query = "INSERT INTO users (user_name, email) VALUES (%s, %s);"
            cursor.execute(query, new_customer)
            conn.commit() # commit the transaction
            print(f"New user {name} added successfully")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

