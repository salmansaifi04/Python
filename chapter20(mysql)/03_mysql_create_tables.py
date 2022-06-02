import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'salman@123',
    database = 'mydatabase'
)

mycursor = db.cursor()

## how to create table
# mycursor.execute('create table customers(name varchar(255), address varchar(255))')


## how to check table exist or not
# mycursor.execute('show tables')
# for x in mycursor:
#     print(x) 

## how to add primary key  using alter table

# mycursor.execute('alter table customers add column id int auto_increment primary key') 


mycursor.execute('create table customers(id int auto_increment primary key,name varchar(255), address varchar(255))')