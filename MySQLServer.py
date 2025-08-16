import mysql.connector
from mysql.connector import Error

def create_database():
    connection = None
    try:
        # Connect to MySQL server (edit user/password/host if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"
        )

        if connection.is_connected():
            cursor = connection.cursor()
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Safely close connection
        if connection is not None and connection.is_connected():
            cursor.close()
            connection.close()
            # print("MySQL connection is closed")   # optional

if _name_ == "_main_":
    create_database()
