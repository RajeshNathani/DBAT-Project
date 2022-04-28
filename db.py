from sqlite3 import connect

import mysql.connector

def connectBooks():
    mydb = mysql.connector.connect(
    host="localhost",
    user="rajesh",
    password="1234",
    database = "books"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM books")
    myresult = mycursor.fetchall()
    return myresult

def connectUsers():
    mydb = mysql.connector.connect(
    host="localhost",
    user="rajesh",
    password="1234",
    database = "books"
    )

    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM users")
    myresult = mycursor.fetchall()
    return myresult

def addUsers(name, email, password):
    mydb = mysql.connector.connect(
    host="localhost",
    user="rajesh",
    password="1234",
    database = "books"
    )

    mycursor = mydb.cursor()
    sql = "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)"
    val = (name,email,password)
    mycursor.execute(sql, val)
    mydb.commit()