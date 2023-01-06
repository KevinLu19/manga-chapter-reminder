from fastapi import FastAPI

import mangadex_api.manga_id as mangadex_api
import mangadex_api.manga_chapters as manga_chapter
import mysql_database.database as db
import mysql_database.database as db_chapter

# app = FastAPI()

# @app.get("/")
# async def root():
#     return {"message": "Hello world"}


if __name__ == "__main__":

    while True:
        userinput = input("Enter in manga names to be stored in database (press q to exit): ")
        
        if userinput == "Q" or userinput == "q":
            break
        
        # Feeds user input into the manga title class.
        manga_title = mangadex_api.MangaTitle(userinput)
        list_manga_id = manga_title.get_manga_title()

        # User input stores into the database.
        manga_database = db.Database()
        manga_database.add_into_database(str(userinput))

        # print (list_manga_id)

        manga_chapter = manga_chapter.MangaChapter()
        # manga_chapter.manga_id_cleanup(list_manga_id)
        manga_chapter.get_manga_chapter(list_manga_id)