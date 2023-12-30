import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="936700",
    database="DBbusCommPtr"
)
mycursor=mydb.cursor()