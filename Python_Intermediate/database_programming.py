import sqlite3

connection = sqlite3.connect('mydb.db')
cursor = connection.cursor()
cursor.execute("select * from person")
results = cursor.fetchall()
print(results)
cursor.close()
connection.close()
