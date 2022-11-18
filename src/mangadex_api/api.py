import manga_search_api

BASE_URL = "https://api.mangadex.org"
temp_manga_title = "blue lock"   


if __name__ == "__main__":
    manga_search_obj = manga_search_api.MangaTitle()
    manga_search_obj.search_manga_title()