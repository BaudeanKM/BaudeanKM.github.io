import sqlite3
# Deal with errors
try:
	connection = sqlite3.connect("C:\\Users\Ken\Desktop\BaudeanKM.github.io\Data_base_sqlite.db")
	cursor = connection.cursor()
	
	req = cursor.execute('SELECT *FROM uers')
	
	for row in req.fetchall():
		print(row[1])
except Exception as e:
	print("[ERREUR]", e)
	connection.rollback()
	# Rollback if it didn't workedout
finally:
	connection.close()
