import sqlite3

import pyodbc
import mysql.connector

def connect_to_mysql():
    try:
        connection = mysql.connector.connect(
            host="your_mysql_host",  # e.g., "localhost" or IP address
            user="your_username",
            password="your_password",
            database="your_database"
        )

        if connection.is_connected():
            print("Connected to MySQL database")
            # Your database operations go here
            cursor = connection.cursor()
            cursor.execute("SELECT DATABASE();")
            db = cursor.fetchone()
            print(f"You're connected to database: {db}")
            
    except mysql.connector.Error as err:
        print(f"Error: {err}")
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("Connection closed")

connect_to_mysql()

def connect_to_sql_server(server_name, database_name, user_name, password_):
    try:
        connection = pyodbc.connect(
            driver="{ODBC Driver 17 for SQL Server}",
            server=server_name,  
            database= database_name,
            user=user_name,
            password=password_
        )

        cursor = connection.cursor()
        cursor.execute("SELECT @@VERSION;")
        db_version = cursor.fetchone()
        print(f"Connected to SQL Server, version: {db_version}")
        
    except pyodbc.Error as err:
        print(f"Error: {err}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection closed")

def connect_to_sqlite(my_connection):
    try:
        connection = sqlite3.connect(my_connection)

        cursor = connection.cursor()
        cursor.execute("SELECT sqlite_version();")
        db_version = cursor.fetchone()
        print(f"Connected to SQLite database, version: {db_version}")
        
    except sqlite3.Error as err:
        print(f"Error: {err}")
    finally:
        if connection:
            cursor.close()
            connection.close()
            print("Connection closed")

def main(): 
    print("Chọn db bạn muốn kiểm tra:\n")
    print("1. sqlite\n")
    print("2. mysql\n")
    print("3. sql server\n")
    print("4. Posgret\n")
    name_db = input(int())
    connection_name = input("Chuỗi kết nối của bạn : ")
    if(name_db == 1):
        connect_to_sqlite(connection_name)
    elif(name_db == 3):
        ser_name = input("sever name: \n")
        db_name = input("Database : \n")
        username = input("user name:\n")
        pass_w = input("password :\n")
        connect_to_sql_server(ser_name,db_name,username,pass_w)
    elif(name_db == 2):
        connect_to_mysql()


if __name__ == "__main__":
    main()
