import sqlite3

connection = sqlite3.connect("C:\\Users\Ken\Desktop\BaudeanKM.github.io\Data_base_sqlite.db")
# The file isn't in the python folder so we need to collect it 
cursor = connection.cursor()

my_username = ("Ken",)

cursor.execute('SELECT * FROM the_users WHERE user_name = ?', my_username)
result = cursor.fetchone()[1]
# Allow us to return the element picked between the brackets. 
print(f"Le nom d'utilisateur est : {result}")

connection.close()
