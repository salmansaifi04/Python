import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'salman@123',
    db = 'mydatabase'
)

mycursor = db.cursor()

## how insert values into table in one row 
# sql = ('insert into customers (name, address) values(%s, %s)')
# val = ('salman', 'Greater Noida') 
# mycursor.execute(sql,val)

## Insert multiple rows

# sql = ('insert into customers (name, address) values(%s, %s)')
# val = [
#     ('anjali', 'near dasna'),
#     ('nitin', 'near dasna'),
#     ('vishal', 'ghaziabad'),
#     ('shubham', 'modinagar')
# ]


# mycursor.executemany(sql, val)
# db.commit()

print(mycursor.rowcount, "was inserted")

db.commit()