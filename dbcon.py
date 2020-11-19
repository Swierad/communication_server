from psycopg2 import connect, OperationalError
from config import dbdata



def db_connect(db):
    try:
        # creating connection
        cnx = connect(user=dbdata['user'],
                      password=dbdata['coderslab'],
                      host=dbdata['localhost'],
                      database=dbdata[db]
                      )
        print("Połączenie udane.")
        cnx.close()
    except OperationalError:
        print("Nieudane połączenie.")