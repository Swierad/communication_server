from psycopg2 import connect, OperationalError
from config import dbdata




def db_connect(db='com_server'):
    try:
        # creating connection
        cnx = connect(user=dbdata['user'],
                      password=dbdata['password'],
                      host=dbdata['host'],
                      database=dbdata['db']
                      )
        cnx.autocommit = True
        return cnx
    except OperationalError:
        print("Nieudane połączenie.")