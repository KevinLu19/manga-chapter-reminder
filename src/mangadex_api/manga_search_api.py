import api      # Once database is setup, retreive manga name from the database instead from hard code.
import requests

class MangaTitle:
    def __init__(self):
        pass
    
    # ----------------------------------------
    # Public Methods
    # ----------------------------------------
    def search_manga_title(self):
        req = requests.get(f"{api.BASE_URL}/manga/", params={"title": api.temp_manga_title})
        manga_title_id = [manga["id"] for manga in req.json()["data"]]

        return manga_title_id
