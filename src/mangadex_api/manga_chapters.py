import requests
# import mysql_database.database as db

class MangaChapter:
    BASE_URL = "https://api.mangadex.org"

    def __init__(self, manga_id: list):
        self.__manga_id = ""
        self.manga_name = ""
        self.chapter = ""
        self.readable_at = ""       # Format is yyyy-mm-dd hh:mm::ss
        
        self.latest_chapter = ""
        self.latest_chapter_readable_at = ""   # Format is yyyy-mm-dd hh:mm::ss
        
        # If there's no value for latest chapter, then we fetch the latest chapter. Otherwise, don't need to fetch latest chapter again.
        # Need to track manga name/ id in this condition. Otherwise, the next entry from database will return back null since latest chapter variable will have value.
        # if self.latest_chapter and self.latest_chapter_readable_at == None:
        #     self.get_manga_chapter(
        # else:
        #     pass

    # ----------------------------------------
    # Public Methods
    # ----------------------------------------
    
    def get_manga_ids(self, manga_ids: list):
        for manga_ids in manga_ids:
            for manga_id in manga_ids:
                self.__manga_id = manga_id
        
        print (self.__manga_id)

    def get_manga_chapter(self, manga_ids: list):
        temporary_manga_id = "b4c93297-b32f-4f90-b619-55456a38b0aa"     # Later on, grab this from database.
        langauge = ["en"]
        
        chapter_list = []
        chapter_readable_time = []

        # Iterates through list of manga ids within a lists. 
        for manga_ids in manga_ids:
            for manga_id in manga_ids:
                
                self.__manga_id = manga_id

                req = requests.get(f"{self.BASE_URL}/manga/{self.__manga_id}/feed", params={"translatedLanguage[]": langauge},)
                manga_chapter_attributes = [chapter["attributes"] for chapter in req.json()["data"]]
                    
    
        for chapter in manga_chapter_attributes:
            chapter_list.append(float(chapter["chapter"]))
            chapter_readable_time.append(chapter["readableAt"])

        self.get_biggest_chapter(chapter_list)
        self.get_biggest_readable(chapter_readable_time)

    # Helper function which stores the current largest readable time to compare with upcoming chapters/ readable times.
    # Might need to change the type of readable_time from <str> to a <time> format as this could potentially cause issues in the future when comparing.
    def get_biggest_readable(self, readable_time: list) -> None:
        readable_time.sort()
        self.latest_chapter_readable_at = readable_time[-1]

        print("Current readable time: ", readable_time[-1])
        print ("#############")

    # Helper function which stores the current largest chapter to compare with upcoming chapters.
    def get_biggest_chapter(self, list_of_chapters: list) -> None:
        list_of_chapters.sort()
        sorted_chapter = ["%g" % number for number in list_of_chapters]         # Removes trailing 0s in a float.

        self.latest_chapter = sorted_chapter[-1]
        print ("#############")
        print("Manga Name: ", self.__manga_id)
        print("Current Latest Chapter: ",  sorted_chapter[-1])

    # Use this to helper function to retreive the next largest chapter if there is one.
    def save_current_largest_chapter(self):
        pass

        
    # ----------------------------------------
    # Private Methods
    # ----------------------------------------


if __name__ == "__main__":
    manga_chapt = MangaChapter()
    manga_chapt.get_manga_chapter()