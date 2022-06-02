import pymysql

mydb = pymysql.connect(
    host='localhost',
    user = 'root',
    password = 'salman@123'
)

print(mydb)

