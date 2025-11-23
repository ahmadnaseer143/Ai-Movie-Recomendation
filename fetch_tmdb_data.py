import requests
import pandas as pd

TMDB_API_KEY = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIyM2I5NzE1MjJmZjZkOTkxOGQwNWFkMjg0MzA5ZjhhYiIsIm5iZiI6MTY0Mzg4MTYzMS45OTksInN1YiI6IjYxZmJhNDlmMGM0YzE2MDEwOTgwODVkZCIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.OXL3l701nRktTJey4KfrovfMmXVbyBAtco8QQwTv04Y"  # Replace with your Key (Bearer)
BASE_URL = "https://api.themoviedb.org/3"

def fetch_tmdb_movies(page=1):
    url = f"{BASE_URL}/movie/popular?language=en-US&page={page}"

    headers = {
        "accept": "application/json",
        "Authorization": f"Bearer {TMDB_API_KEY}"
    }

    response = requests.get(url, headers=headers)
    data = response.json()

    # DEBUG:
    if "results" not in data:
        print("ERROR RESPONSE FROM API:", data)  # PRINT FULL RESPONSE
        return []

    movies = []
    for movie in data["results"]:
        movies.append({
            "title": movie["title"],
            "overview": movie.get("overview", ""),
            "genres": ",".join(str(g) for g in movie.get("genre_ids", []))
        })

    return movies

# Fetch 3 pages (~60 movies)
all_movies = []
for i in range(1, 4):
    all_movies.extend(fetch_tmdb_movies(page=i))

df = pd.DataFrame(all_movies)
df.to_csv("tmdb_movies.csv", index=False)
print("TMDB data saved to tmdb_movies.csv")
