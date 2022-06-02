import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'salman@123',
    db = 'mydatabase'
)

mycursor = db.cursor()

## ---- how to select data from table using 'fetchall method' ----
# mycursor.execute('select * from customers')
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)

## ---- how select columns 'fetchall method' ----

# mycursor.execute('select name, address from customers')
# myresult = mycursor.fetchall()
# for x in myresult:
#     print(x)


## --- fetchone method ---
# mycursor.execute('select * from customers')
# myresult = mycursor.fetchone()
# print(myresult)