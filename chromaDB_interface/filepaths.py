import os

COLLECTION_NAME = "movies_collection"

chroma_data_base_path = os.path.join("chromaDB_vec_db")


# json_film_data_main = os.path.join("json_data", "films_data.json")

json_genre_ids = os.path.join("json_data", "genres_ids.json")
json_film_data_w_keywords = os.path.join('json_data', 'films_data_w_keywords.json')

# backup of the original film data, don't use or change if nescessary
json_films_backup = os.path.join("json_data", "films_data_backup.json")

if __name__=="__main__":
    pass