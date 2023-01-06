import requests
import mysql_database.database as db

class MangaTitle:
    BASE_URL = "https://api.mangadex.org"

    def __init__(self, user_input: str):
        self._mysql_database = db.Database()
        self.__user_input = user_input

    # ----------------------------------------
    # Public Methods
    # ----------------------------------------
    
    # Compares users input to the title from request. 
    # Want to prevent side mangas that keep appearing because request matches with one word within the title in the api.
    # Task: Want to incorporate symbol removal with the comparison to make a little easier when comparing two words.

    # This function didn't work. Need to re-visit.
    def manga_name_comparison(self, request_data : list):
        upper_case_user_input = self.__user_input.upper()

        # print (request_data)

        manga_title_id_list = []

        for items in request_data:
            holding_manga_id = items["id"]
            request_data_manga_name = items["attributes"]["title"]["en"].upper()       

            if upper_case_user_input == request_data_manga_name:
                # print (request_data_manga_name)
                # print ("Manga ID: ", holding_manga_id)
                manga_title_id_list.append(holding_manga_id)

        return manga_title_id_list

    def get_json_raw_data(self):
        manga_title_of_tuple = self._mysql_database.fetch_specified_manga_title(self.__user_input)            

        for manga_title in manga_title_of_tuple:
            req = requests.get(f"{self.BASE_URL}/manga/", params={"title": manga_title})    # Finds the ID of manga title
            raw_request_data = req.json()["data"]
            self.manga_name_comparison(raw_request_data)
        
        return raw_request_data

    # Retreives manga ID from request module.
    def get_manga_title(self):
        # This returns back the manga name in a tuple form.
        # manga_title_of_tuple = self._mysql_database.fetch_specified_manga_title(self.__user_input)            

        req_raw_data = self.get_json_raw_data()

        manga_id_list = []

        for manga_id in req_raw_data:
            # print (manga_id["id"])
            manga_id_list.append(manga_id["id"])

        return manga_id_list

    # ----------------------------------------
    # Private Methods
    # ----------------------------------------

if __name__ == "__main__":
    mangatitle_obj = MangaTitle()
    #mangatitle_obj.get_manga_title("ayakashi triangle")
    mangatitle_obj.get_manga_title()