import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'salman@123',
    db = 'mydatabase'
)

mycursor = db.cursor()

## ---- how to update table -----
# sql = "update customers set address = 'near dasna ghaziabad' where name = 'anjali'"

# mycursor.execute(sql)
# db.commit()
# print(mycursor.rowcount)