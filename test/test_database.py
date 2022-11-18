import unittest
import mysql.connector
import os


class TestDatabase(unittest.TestCase):
    def setup(self) -> None:
        try:
            self.conn = mysql.connector.connect(host="localhost", user = f"{os.environ.get('DATABASE_USERNAME')}", password = f"{os.environ.get('DATABASE_PASSWORD')}", database="manga_chapters")
            print("Connected to the database.")

        except mysql.connector.errors as err:
            print(err.msg)