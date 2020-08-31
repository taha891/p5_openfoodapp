import mysql.connector


def init_database():

    openfood_db = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="banane35",
    )

    print(openfood_db)

    mycursor = openfood_db.cursor()

    mycursor.execute("DROP DATABASE IF EXISTS openfooddb")
    mycursor.execute("CREATE DATABASE IF NOT EXISTS openfooddb")