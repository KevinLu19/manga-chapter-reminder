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

    # def get_manga_title_id(self):
    #     manga_title_in_list_of_tuple = self._mysql_database.fetch_all_manga_title()

    #     manga_title_id_list = []

    #     for manga_title_tuple in manga_title_in_list_of_tuple:
    #         for manga_title in manga_title_tuple: 
    #             req = requests.get(f"{self.BASE_URL}/manga/", params={"title": manga_title})
    #             manga_title_id = [manga["id"] for manga in req.json()["data"]]
    #             manga_title_id_list.append(manga_title_id)
            
    #     return manga_title_id_list
    
    # Compares users input to the title from request. 
    # Want to prevent side mangas that keep appearing because request matches with one word within the title in the api.
    # Task: Want to incorporate symbol removal with the comparison to make a little easier when comparing two words.
    def manga_name_comparison(self, request_data : list):
        upper_case_user_input = self.__user_input.upper()

        print (request_data)

        manga_title_id_list = []

        for items in request_data:
            holding_manga_id = items["id"]
            request_data_manga_name = items["attributes"]["title"]["en"].upper()       

            if upper_case_user_input == request_data_manga_name:
                # print (request_data_manga_name)
                # print ("Manga ID: ", holding_manga_id)
                manga_title_id_list.append(holding_manga_id)
        
        
        return manga_title_id_list


    def get_manga_title(self):
        # manga_title_in_list_of_tuple = self._mysql_database.fetch_all_manga_title()
        manga_title_in_list_of_tuple = self._mysql_database.fetch_specified_manga_title(self.__user_input)
        
        for manga_title_tupe in manga_title_in_list_of_tuple:
            for manga_title in manga_title_tupe:
                req = requests.get(f"{self.BASE_URL}/manga/", params={"title": manga_title})
                raw_request_data = req.json()["data"]
                self.manga_name_comparison(raw_request_data)

        # manga_title_id = [manga["id"] for manga in req.json()["data"]] 
        # actual_manga_title_list = [manga["attributes"]["title"]["en"] for manga in req.json()["data"]]


        #print (actual_manga_title_list)

    # ----------------------------------------
    # Private Methods
    # ----------------------------------------

# Temporary stuff
# def main():
#     while True:
#         userinput = input("Enter in manga names to be stored in database (press q to exit):  ")
        
#         if userinput == "Q" or userinput == "q":
#             break
        
#         manga_title = MangaTitle()
#         manga_title.get_manga_title_id()

#         database = db.Database()
#         database.add_into_database(userinput)

if __name__ == "__main__":
    mangatitle_obj = MangaTitle()
    #mangatitle_obj.get_manga_title("ayakashi triangle")
    mangatitle_obj.get_manga_title()