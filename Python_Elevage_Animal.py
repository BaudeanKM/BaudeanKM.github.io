import mysql.connector as MC

try:
    conn = MC.connect(host = 'louise', database = 'elevage',user = 'root',password = 1507666 )
    cursor = conn.cursor()

    req ='SELECT * FROM animal'
    cursor.execute(req)

    animal = cursor.fetchall()

    for n in animal:
        print('espece : {}'.format(espece[1]))
except MC.Error as err :
    print(err)
finally:
    if(conn.is_connected()):
        cursor.close()
        conn.close()