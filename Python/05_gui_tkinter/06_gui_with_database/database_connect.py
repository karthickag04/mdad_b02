import mysql.connector
from mysql.connector import Error

# db connection with Try Except

def connect_to_database():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='192.168.29.244',
            database='a',
            user='test01',
            password='test@123'
        )
        if connection.is_connected():
            print("Connection Status: Connected to MySQL database")
    except Error as e:
        if "Access denied" in str(e):
            print("Error: Invalid username or password")
        elif "Unknown database" in str(e):
            print("Error: Database does not exist")
        else:
            print(f"Error connecting to MySQL: {e}")
    finally:
        if connection and connection.is_connected():
            connection.close()
            print("Connection closed")
    
    return connection

print("Connection established at :",connect_to_database())


# method to connect db without try except and return connection

def MyDBConnection():
    dbcon=mysql.connector.connect(
    host="192.168.29.244",
    user="test01",
    password="test@123",
    database="a"
    )

    return dbcon

print("Connection Established at :", MyDBConnection())





