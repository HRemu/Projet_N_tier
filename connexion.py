import mysql.connector as mysql

## connecting to the database using 'connect()' method
## it takes 3 required parameters 'host', 'user', 'passwd'
db = mysql.connect(
    host = "localhost",
    user = "etudiant",
    password = "mdpntiers",
    database = "stageetudiant",
    auth_plugin = 'mysql_native_password'
)

cursor = db.cursor()
cursor.execute("SELECT * FROM INTERNSHIP;")

print(cursor.fetchall())
