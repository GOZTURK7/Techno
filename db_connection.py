import mysql.connector
import config

mydb = mysql.connector.connect(
    host = config.HOST,
    user = config.USER,
    port = config.PORT,
    password = config.PASSWORD,
    database = config.DATABASE
)

print(mydb)
if mydb.is_connected():
    print("Database is connected.")

mycursor = mydb.cursor()

query = 'select * from student'
mycursor.execute(query)
rows = mycursor.fetchall()
print(rows)
for row in rows:
    print(row)