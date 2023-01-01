from mysql.connector import errorcode
from decouple import config

import mysql.connector

class Database:
    def __init__(self):
        print("-------------------------")
        self.conn = mysql.connector.connect(host="localhost", user=config("DATABASE_USERNAME"), password=config("DATABASE_PASSWORD"), database="manga_chapter")
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
        SQL_COMMAND = f"INSERT IGNORE INTO manga_name(name) VALUES(%s);" 
        VALUE = manga_title

        try:
            self.cursor.execute(SQL_COMMAND, (VALUE,))
            self.conn.commit()
            print("-----------------")
            print(f"Added {VALUE} into the table.")
            print("-----------------")
        
        except mysql.connector.Error as err:
            print(f"mysql exception: {err}")
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

class LatestMangaChapter:
    def __init__(self):
        print("-------------------")
        self.conn = mysql.connector.connect(host="localhost", user=config("DATABASE_USERNAME"), password=config("DATABASE_PASSWORD"), database="manga_chapter")
        print("Logged into Latest Chapter Table.")
        print("-------------------")

        self.cursor = self.conn.cursor()

        try:
            SQL_COMMAND = "CREATE TABLE IF NOT EXISTS latest_chapter (name VARCHAR(255), chapter_number INT)"
            self.cursor.execute(SQL_COMMAND)

        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("Table already created.")
            else:
                print(err.msg)

    # ----------------------------------------
    # Public Methods
    # ----------------------------------------
    def verify_name_in_database(self, manga_name_str):
        SQL_COMMAND = f"SELECT * FROM lastest_chapter WHERE NAME={manga_name_str}"


    def update_latest_manga_chapter(self):
        pass

    # ----------------------------------------
    # Private Methods
    # ----------------------------------------
    def __add_entry(self, manga_name: str, latest_manga_chapter: int):
        SQL_COMMAND = f"INSERT INGNORE INTO latest_chapter(name, chapter_number) VALUES(%s, %i)"


if __name__ == "__main__":
    print(f"Database Pass: {config('DATABASE_PASSWORD')}")
    print(f"Database User: {config('DATABASE_USERNAME')}")
    # database = Database()
    latest_chpt = LatestMangaChapter()
