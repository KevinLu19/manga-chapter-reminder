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
    
    # Fetches the manga Id from user input which stores into the database.
    mangadex_api = mangadex_api.MangaTitle()
    list_manga_id = mangadex_api.get_manga_title_id()

    # Fetches the manga chapter using the ID from manga ID class.
    manga_chapter = manga_chapter.MangaChapter()
    manga_chapter.manga_id_cleanup(list_manga_id)
    manga_chapter.get_manga_chapter()

    # manga_database = db.Database()
    # latest_chapter_database = db_chapter.LatestMangaChapter()

    # if manga_chapter.latest_chapter_int is None:
    #     manga_chapter.get_manga_chapter(list_manga_id)
    # else:
    #     manga_database.fetch_all_manga_title()