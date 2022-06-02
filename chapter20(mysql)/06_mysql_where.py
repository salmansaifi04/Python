import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'salman@123',
    db = 'mydatabase'
)

mycursor = db.cursor()

## ---- select with a filter ----
# mycursor.execute("select * from customers where address = 'near dasna'")
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)


## ---- wildcard character -----
# mycursor.execute("select * from customers where address like 'n%'")
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)

