import mysql.connector
from mysql.connector import Error 


class dbconnection():
    def dbconn(self):
        try:
            cnx = mysql.connector.connect(
                user='test01',
                password='test@123',
                host='192.168.29.244',
                database='a'
                )
        except Error as e:
            if "Access Denied" in e:
                print("Username and password error")
            else:
                print("Error while connecting to MySQL", e)
        else:
            return cnx
