import requests
import mysql_database.database as db

class MangaTitle:
    BASE_URL = "https://api.mangadex.org"

    def __init__(self):
        self._mysql_database = db.Database()
    
    # ----------------------------------------
    # Public Methods
    # ----------------------------------------

    def get_manga_title_id(self):
        manga_title_in_list = self._mysql_database.fetch_all_manga_title()

        for manga_title in manga_title_in_list:
            req = requests.get(f"{self.BASE_URL}/manga/", params={"title": manga_title})
            manga_title_id = [manga["id"] for manga in req.json()["data"]]
            
        return manga_title_id
    
    # ----------------------------------------
    # Private Methods
    # ----------------------------------------



# Temporary stuff
def main():
    while True:
        userinput = input("Enter in manga names to be stored in database (press q to exit):  ")
        
        if userinput == "Q" or userinput == "q":
            break

        database = db.Database()
        database.add_into_database(userinput)