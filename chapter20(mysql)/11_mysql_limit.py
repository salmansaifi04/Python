import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'salman@123',
    db = 'mydatabase'
)

mycursor = db.cursor()

## --- how select from table using 'limit' ---
# sql = "select * from customers limit 2"
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)


## ---- start from another position ----

# sql = "select * from customers limit 4 offset 2 "
# mycursor.execute(sql)
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)
