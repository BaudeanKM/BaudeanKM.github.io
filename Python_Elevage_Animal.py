"""
cursor.rowcount
cursor.lastrowid
"""
import mysql.connector as MC

try:
    conn = MC.connect( host = 'localhost', database = 'elevage', user = 'root', password = '' )
    cursor = conn.cursor()

    req ='SELECT * FROM animal'
    cursor.execute(req)

    animal = cursor.fetchall()

    for categorie in animal:
        print('especes : {}'.format(categorie[1]))
except MC.Error as err :
    print(err)
finally:
    if(conn.is_connected()):
        cursor.close()
        conn.close()