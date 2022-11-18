from mysql.connector import errorcode

import mysql.connector
import os

class Database:
    def __init__(self):
        print("-------------------------")
        self.conn = mysql.connector.connect(host="localhost", user=f"{os.environ.get('DATABASE_USERNAME')}", password=f"{os.environ.get('DATABASE_PASSWORD')}", database="manga_chapters")
        print("Logged into the database")
        print("-------------------------")

        self.cursor = self.conn.cursor()

        try:
            SQL_COMMAND = "CREATE TABLE IF NOT EXISTS manga_name (name VARCHAR(255))"
            self.cursor.execute(SQL_COMMAND)
        
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print ("Already exists.")
            else:
                print(err.msg)

    # ----------------------------------------
    # Public Methods
    # ----------------------------------------

    def fetch_manga_title(self):
        pass



    # ----------------------------------------
    # Private Methods
    # ----------------------------------------
    def __add_manga_title(self, manga_title):
        pass

    def __drop_table(self):
        pass

    def __add_unique_identifier_to_column(self):
        SQL_COMMAND = "ALTER TABLE manga_name ADD UNIQUE INDEX(name)"
        self.cursor.execute(SQL_COMMAND)
    
    def __exit__(self):
        if self.conn is not None and self.conn.is_connected():
            print("=====================")
            print("Closing connection to the databse.")
            print("=====================")
            self.conn.close()