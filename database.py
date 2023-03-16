import mysql.connector

DB=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="school"
)
CR=DB.cursor(dictionary=True)
