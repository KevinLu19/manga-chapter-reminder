# import manga_id
import requests
# import mysql_database.database as db

class MangaChapter:
    BASE_URL = "https://api.mangadex.org"

    def __init__(self):
        # self.__manga_id = manga_id
        self.chapter = ""
        self.readable_at = ""       # Format is yyyy-mm-dd hh:mm::ss
        
        self.largest_chapter = ""
        self.largest_chapter_readable_at = ""   # Format is yyyy-mm-dd hh:mm::ss

    # ----------------------------------------
    # Public Methods
    # ----------------------------------------

    def get_manga_chapter(self):
        temporary_manga_id = "b4c93297-b32f-4f90-b619-55456a38b0aa"     # Later on, grab this from database.
        langauge = ["en"]
        
        req = requests.get(f"{self.BASE_URL}/manga/{temporary_manga_id}/feed", params={"translatedLanguage[]": langauge},)
        manga_chapter_attributes = [chapter["attributes"] for chapter in req.json()["data"]]

        # print(self.sort_manga_chapter(manga_chapter_attributes))
        chapter_list = []
        chapter_readable_time = []

        for chapter in manga_chapter_attributes:
            # print(chapter["volume"], chapter["chapter"], chapter["readableAt"])
            # print("Chapter: ", float(chapter["chapter"]))

            chapter_list.append(float(chapter["chapter"]))
            chapter_readable_time.append(chapter["readableAt"])

        self.get_biggest_chapter(chapter_list)
        self.get_biggest_readable(chapter_readable_time)
            # self.get_biggest_chapter(float(chapter["chapter"]))
            
            # print("Readable At: ", chapter["readableAt"])

    # Helper function which stores the current largest readable time to compare with upcoming chapters/ readable times.
    # Might need to change the type of readable_time from <str> to a <time> format as this could potentially cause issues in the future when comparing.
    def get_biggest_readable(self, readable_time):
        readable_time.sort()
        self.largest_chapter_readable_at = readable_time[-1]

        print(type(readable_time[-1]))

    # Helper function which stores the current largest chapter to compare with upcoming chapters.
    def get_biggest_chapter(self, chapters):
        chapters.sort()
        sorted_chapter = ["%g" % number for number in chapters]

        self.largest_chapter = sorted_chapter[-1]
        print(sorted_chapter[-1])

        # print("%g" % largest_chapter)

    # Use this to helper function to retreive the next largest chapter if there is one.
    def save_current_largest_chapter(self):
        pass


    def convert_dict_to_list(self, manga_dictionary):
        return [{key: value} for key, value in manga_dictionary.items()]
               
    # ----------------------------------------
    # Private Methods
    # ----------------------------------------


if __name__ == "__main__":
    manga_chapt = MangaChapter()
    manga_chapt.get_manga_chapter()