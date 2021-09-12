import sqlite3

try:
	connection = sqlite3.connect("C:\\Users\Ken\Desktop\BaudeanKM.github.io\Data_base_sqlite.db")
	# The file isn't in the python folder so we need to collect it 
	cursor = connection.cursor()

	les_joueurs = 'SELECT user_name FROM the_users'
	cursor.execute(les_joueurs)
	result = cursor.fetchall()
	# Allow us to return the element picked between the brackets. 
	for row in result:
		print(row[0])
except Exception as e:
	print("[ERREUR]", e)
	connection.rollback()
	# Rollback if it didn't workedout
finally:
	connection.close()
