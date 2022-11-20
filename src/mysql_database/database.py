from mysql.connector import errorcode

import mysql.connector
import os

class Database:
    def __init__(self):
        print("-------------------------")
        self.conn = mysql.connector.connect(host="localhost", user="root", password="tifalockhart", database="manga_chapter")
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
    def fetch_all_manga_title(self):
        SQL_COMMAND = f"SELECT name FROM manga_name"
        self.cursor.execute(SQL_COMMAND)

        return self.cursor.fetchall()

    def add_into_database(self, manga_title):
        self.__add_entry(manga_title)           # Protection of private member of private member function of database.

    # ----------------------------------------
    # Private Methods
    # ----------------------------------------
    def __add_entry(self, manga_title):
        SQL_COMMAND = f"INSERT IGNORE INTO manga_name(name) VALUES('{manga_title}');" 

        try:
            self.cursor.execute(SQL_COMMAND)
            print("-----------------")
            print(f"Added {manga_title} into the table.")
            print("-----------------")

            self.conn.commit()
        
        except mysql.connector.Error as err:
            print(err.msg)
            self.conn.rollback()

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

if __name__ == "__main__":
    database = Database()