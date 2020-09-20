import mysql.connector
from config import HOST, USER, PASSWD, DATABASE


class Database:

    def __init__(self):
        self.openfood_db = mysql.connector.connect(
            host=HOST,
            user=USER,
            passwd=PASSWD,
            database=DATABASE
        )

        self.mycursor = self.openfood_db.cursor()

    ''' Create table for the products and categories'''

    def create_table(self):
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS products ("
                              "code_bar VARCHAR(255),"
                              "name VARCHAR(255),"
                              "nutriscore SMALLINT,"
                              "url VARCHAR(250),"
                              "stores LONGTEXT,"
                              "PRIMARY KEY (code_bar))"
                              "DEFAULT CHARSET=utf8 ENGINE = InnoDB")
        self.mycursor.execute("CREATE TABLE IF NOT EXISTS category ("
                              "name VARCHAR(255),"
                              "PRIMARY KEY (name))"
                              "CHARSET=utf8 ENGINE = InnoDB")

        self.mycursor.execute("CREATE TABLE IF NOT EXISTS association ("
                              "code_asso INT UNSIGNED NOT NULL AUTO_INCREMENT,"
                              "id_product VARCHAR(255) DEFAULT 1,"
                              "id_category VARCHAR(255) DEFAULT 2,"
                              "PRIMARY KEY(code_asso))"
                              "CHARSET=utf8 ENGINE = InnoDB")
        self.openfood_db.commit()

        self.mycursor.execute("CREATE TABLE IF NOT EXISTS substitute ("
                              "id_substitute INT UNSIGNED NOT NULL "
                              "AUTO_INCREMENT,"
                              "id_product VARCHAR(255),"
                              "substitute VARCHAR(255),"
                              "PRIMARY KEY(id_substitute))"
                              "CHARSET=utf8 ENGINE = InnoDB")

        self.mycursor.execute("""ALTER TABLE association
                              ADD CONSTRAINT FK_category
                              FOREIGN KEY (id_category)
                              REFERENCES category(name)""")
        self.mycursor.execute("""ALTER TABLE association
                              ADD CONSTRAINT FK_product
                              FOREIGN KEY (id_product)
                              REFERENCES products(code_bar)""")
        self.openfood_db.commit()

        self.mycursor.execute("""ALTER TABLE substitute
                              ADD CONSTRAINT FK_product_selected
                              FOREIGN KEY (id_product)
                              REFERENCES products(code_bar)""")
        self.mycursor.execute("""ALTER TABLE substitute
                              ADD CONSTRAINT FK_substitute
                              FOREIGN KEY (substitute)
                              REFERENCES products(code_bar)""")
        self.openfood_db.commit()
