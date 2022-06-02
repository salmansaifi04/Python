import pymysql

db = pymysql.connect(
    host = 'localhost',
    username = 'root',
    password = 'salman@123' 
)

mycursor = db.cursor()

## how to create database   
# mycursor.execute('create database mydatabase')

## check if database exist or not
mycursor.execute('show databases')
for  x in mycursor:
    print(x)

