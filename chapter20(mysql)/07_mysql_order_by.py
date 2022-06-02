import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'salman@123',
    db = 'mydatabase'
)

mycursor = db.cursor()

## ----- order by aesc ----
# mycursor.execute('select * from customers order by name')
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)


## ----- order by desc ----
# mycursor.execute('select * from customers order by name desc')
# myresult = mycursor.fetchall()
# for i in myresult:
#     print(i)