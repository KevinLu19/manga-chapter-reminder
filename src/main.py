import mangadex_api.manga_id as mangadex_api
import mangadex_api.manga_chapters as manga_chapter
import mysql_database.database as db
import mysql_database.database as db_chapter

import gui.gui as gui

if __name__ == "__main__":
    manga_chapter = manga_chapter.MangaChapter()
    
    while True:
        userinput = input("Enter in manga names to be stored in database (press q to exit): ")
        
        if userinput == "Q" or userinput == "q":
            break
        
        # Feeds user input into the manga title class.
        manga_title_obj = mangadex_api.MangaTitle(userinput)
        
        check_user_input = manga_title_obj.check_input_in_database()
        # print("user input from database: ", check_user_input)

        # Return value from the database that is a list.
        if not check_user_input:
            # If cannot find manga from the database, then we add into the database.
            print ("Not currently in the database.")
            db_obj = db.Database()
            db_obj.add_into_database(str(userinput))
            print(f"{userinput} recently added into the database.")
        else:
            list_manga_id = manga_title_obj.get_json_raw_data()
            # print ("Manga ID List: ", list_manga_id)
            manga_chapter.get_manga_chapter(list_manga_id)