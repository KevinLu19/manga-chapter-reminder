import requests
import mysql_database.database as db

class MangaTitle:
    BASE_URL = "https://api.mangadex.org"

    def __init__(self, user_input: str):
        self._mysql_database = db.Database()
        self.__user_input = user_input
        self.manga_title_id_list = []

    # ----------------------------------------
    # Public Methods
    # ----------------------------------------
    
    # Compares users input to the title from request. 
    # Want to prevent side mangas that keep appearing because request matches with one word within the title in the api.
    # Task: Want to incorporate symbol removal with the comparison to make a little easier when comparing two words.
    def manga_name_comparison(self, request_data : list):
        upper_case_user_input = self.__user_input.upper()

        # print (request_data)

        for items in request_data:
            holding_manga_id = items["id"]
            request_data_manga_name = items["attributes"]["title"]["en"].upper()       

            if upper_case_user_input == request_data_manga_name:
                # print (request_data_manga_name)
                # print ("Manga ID: ", holding_manga_id)
                self.manga_title_id_list.append(holding_manga_id)
                print ("Inside the fixed list ", self.manga_title_id_list)

        return self.manga_title_id_list

    # Main function of this class. Executes the request module.
    def get_json_raw_data(self):
        manga_title_of_tuple = self._mysql_database.fetch_specified_manga_title(self.__user_input)            

        # # If canont find manga from the database, then add into the database.
        # if not manga_title_of_tuple:
        #     print ("Not currently in the database.")
        #     self.add_user_input_database()

        for manga_title in manga_title_of_tuple:
            req = requests.get(f"{self.BASE_URL}/manga/", params={"title": manga_title})    # Finds the ID of manga title
            raw_request_data = req.json()["data"]
            self.manga_name_comparison(raw_request_data)
        
        return self.manga_title_id_list
    
    # If database cannot find user input'd data, then we add into the database.
    def add_user_input_database(self):
        self._mysql_database.add_into_database(str(self.__user_input))

    # Checking if user input is in the database already.
    # Possibly throw away function.
    def check_input_in_database(self):
        check_user_input = self._mysql_database.fetch_specified_manga_title(self.__user_input)

        # # Checking the return value from the database.
        # if not check_user_input:
        #     print ("False")
        #     return False
        
        return check_user_input
        

    # ----------------------------------------
    # Private Methods
    # ----------------------------------------

if __name__ == "__main__":
    mangatitle_obj = MangaTitle()
    #mangatitle_obj.get_manga_title("ayakashi triangle")
    mangatitle_obj.get_manga_title()