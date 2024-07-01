from db_connection import db_connection, Error

def fetch_users():
    '''Function to fetch all users from the database.'''
    conn = db_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            query = "SELECT * FROM users;"
            cursor.execute(query)
            for id, name, email in cursor.fetchall():
                print(f"{id}: {name}, {email}")
        except Error as e:
            print(f"Error: {e}")
        finally:
            if conn and conn.is_connected():
                cursor.close()
                conn.close()

def fetch_user():
    '''Function to fetch a specific user from the database.'''
    conn = db_connection()
    if conn is not None:
        try:
            customer_id = input("Enter the name of the user you are searching for: ").title()
            cursor = conn.cursor()
            query = "SELECT * FROM users WHERE user_name = %s;"
            cursor.execute(query, (customer_id,))
            id, name, email = cursor.fetchall()[0]
            print(f"{id}: {name}, {email}")
        except Error as e:
            print(f"Error: {e}")
        finally:
             if conn and conn.is_connected():
                cursor.close()
                conn.close()
if __name__ == "__main__":
    fetch_users()