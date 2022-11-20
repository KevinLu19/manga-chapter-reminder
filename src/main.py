from fastapi import FastAPI

import mangadex_api.manga_search_api as mangadex_api
import mysql_database.database as db

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello world"}


if __name__ == "__main__":
    mangadex_api.main()