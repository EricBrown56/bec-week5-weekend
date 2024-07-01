import mysql.connector # importing mysql connector library that we pip installed
from mysql.connector import Error # importing Error class from mysql connector library 

# Connecting to the database. To establish a connection we need to provide the following details
# CRUD operations
# Create, Retrive, Update, Delete


def db_connection():
    db_name = "library_system"
    db_user = "root"
    db_password = "Groovin"
    db_host = "localhost"

    # Establishing a connection to the database
    try:
        conn = mysql.connector.connect(
            host = db_host,
            user = db_user,
            password = db_password,
            database = db_name
        )

        if conn.is_connected():
            print("Connection established successfully")
            return conn

    except Error as e:
        print(f"Error: {e}")
        return None

   