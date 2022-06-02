import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'salman@123',
    db = 'mydatabase'
)

mycursor = db.cursor()

## ---- how delete record -----
mycursor.execute("delete from customers where address = 'modinagar'")
db.commit()
print(mycursor.rowcount)