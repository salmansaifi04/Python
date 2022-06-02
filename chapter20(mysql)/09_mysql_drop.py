import pymysql

db = pymysql.connect(
    host = 'localhost',
    user = 'root',
    password = 'salman@123',
    db = 'firstdb'
)

mycursor = db.cursor()

## --- how to drop tables ----
# sql = "drop table emp"
# mycursor.execute(sql)


## ---- drop only if exist ----


# sql = "drop table if exists emp"
# mycursor.execute(sql)