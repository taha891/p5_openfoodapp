import mysql.connector
from config import HOST, USER, PASSWD


def init_database():
    ''' Method to create and reset the database '''
    openfood_db = mysql.connector.connect(
        host=HOST,
        user=USER,
        passwd=PASSWD,
    )

    mycursor = openfood_db.cursor()

    mycursor.execute("DROP DATABASE IF EXISTS openfooddb")
    openfood_db.commit()
    mycursor.execute("CREATE DATABASE IF NOT EXISTS openfooddb")
    openfood_db.commit()
