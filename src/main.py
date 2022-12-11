from fastapi import FastAPI

import mangadex_api.manga_id as mangadex_api
import mangadex_api.manga_chapters as manga_chapter
import mysql_database.database as db

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}


if __name__ == "__main__":
    # mangadex_api.main()
    mangadex_api = mangadex_api.MangaTitle()
    list_manga_id = mangadex_api.get_manga_title_id()

    # print(list_manga_id)

    manga_chapter = manga_chapter.MangaChapter()
    manga_chapter.get_manga_chapter(list_manga_id)
