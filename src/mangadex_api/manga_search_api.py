import api
import requests
import json

def search_manga_title():
    req = requests.get(f"{api.BASE_URL}/manga/", params={"title": api.temp_manga_title})
    
    print([manga["id"] for manga in req.json()["data"]])
    