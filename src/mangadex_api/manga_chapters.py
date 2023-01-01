import requests
# import mysql_database.database as db

class MangaChapter:
    BASE_URL = "https://api.mangadex.org"

    def __init__(self):     
        self.cleanup_manga_id_list = []
        self.latest_chapter_int = ""
        self.latest_chapter_readable_at = ""   # Format is yyyy-mm-dd hh:mm::ss
        
    # ----------------------------------------
    # Public Methods
    # ----------------------------------------
    
    # Loops through and places all manga_id into one list.
    # Removes list within list situation.
    def manga_id_cleanup(self, manga_ids: list):
        for manga_ids_list in manga_ids:
            for manga_id in manga_ids_list:
                self.cleanup_manga_id_list.append(manga_id)

        return self.cleanup_manga_id_list

    # Handles the request module requests. 
    def get_request_function(self, manga_id: str):
        language = ["en"]

        chapter_list = []
        chapter_readable_time = []

        req = requests.get(f"{self.BASE_URL}/manga/{manga_id}/feed", params={"translatedLanguage[]": language},)
        manga_chapter_attributes = [chapter["attributes"] for chapter in req.json()["data"]]

        # This block of code actually fetches the chapter from the request module.
        for chapter in manga_chapter_attributes:
            chapter_list.append(float(chapter["chapter"]))
            chapter_readable_time.append(chapter["readableAt"])

            # print (chapter["chapter"])
            # print (chapter_readable_time)
        
            chapter_list.sort()
            chapter_readable_time.sort()

        return chapter_list, chapter_readable_time

    def get_manga_chapter(self):
        temporary_manga_id = "b4c93297-b32f-4f90-b619-55456a38b0aa"     # Later on, grab this from database.

        # Loops through the manga ids and fetches the chapters.
        # Aggregates different parts of the print info block
        for manga_ids in self.cleanup_manga_id_list:
            # print("IDS: ", manga_ids)
            
            manga_chapter_attributes = self.get_request_function(manga_ids)
            # print(manga_chapter_attributes)
            
            readable_manga_name_str = self.get_manga_readable_name(manga_ids)
            
            latest_chatper = self.get_biggest_chapter(manga_chapter_attributes[0], readable_manga_name_str)
            latest_readable_time = self.get_biggest_readable(manga_chapter_attributes[1])

            self.print_latest_chapter_info(manga_ids, readable_manga_name_str, latest_chatper, latest_readable_time)

    # Maps each element of chapter list to it's number counter part.
    def map_manga_chapter_lists(manga_chapter_list : list, manga_chapter_number_list : list):
        return list(map(lambda x, y: x + "" +y, manga_chapter_list, manga_chapter_number_list))

    # Helper function which stores the current largest readable time to compare with upcoming chapters/ readable times.
    # Might need to change the type of readable_time from <str> to a <time> format as this could potentially cause issues in the future when comparing.
    def get_biggest_readable(self, readable_time: list) -> None:
        readable_time.sort()
        self.latest_chapter_readable_at = readable_time[-1]

        # Time in yyyy-mm-ddThh:mm:ss Format
        return readable_time[-1]

        # print("Current readable time: ", readable_time[-1])
        # print ("#############")

    # Helper function which stores the current largest chapter to compare with upcoming chapters.
    def get_biggest_chapter(self, list_of_chapters: list, english_manga_name_str) -> None:
        list_of_chapters.sort()
        sorted_chapter = ["%g" % number for number in list_of_chapters]         # Removes trailing 0s in a float.

        self.latest_chapter_int = sorted_chapter[-1]

        return sorted_chapter[-1]

        # print ("#############")
        # print("Manga ID: ", self.__manga_id)
        # print("Manga Name: ", english_manga_name_str)
        # print("Current Latest Chapter: ",  sorted_chapter[-1])

    def get_manga_readable_name(self, current_manga_id):
        language = ["en"]
        
        req = requests.get(f"{self.BASE_URL}/manga/{current_manga_id}", params={"translatedLanguage[]": language},)
        manga_name = req.json()["data"]["attributes"]["title"]["en"]

        return manga_name

    # Each time we fetch the latest info, we print this block of info.
    def print_latest_chapter_info(self, manga_id, readable_manga_name, latest_chapter, readable_time):
        print ("#############")
        print ("Manga ID: ", manga_id)
        print ("Manga Name: ", readable_manga_name)
        print ("Current Latest Chapter: ", latest_chapter)
        print ("Current Readable Time: ", readable_time)
        print ("#############")

    # Use this to helper function to retreive the next largest chapter if there is one.
    def save_current_largest_chapter(self):
        pass


    # ----------------------------------------
    # Private Methods
    # ----------------------------------------


if __name__ == "__main__":
    manga_chapt = MangaChapter()
   #  manga_chapt.get_manga_chapter()
    print(manga_chapt.get_manga_readable_name("b4c93297-b32f-4f90-b619-55456a38b0aa"))