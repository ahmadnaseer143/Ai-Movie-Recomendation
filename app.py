from fastapi import FastAPI
from recommender import get_recommendations, get_movies
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def test():
    return {"message": "API is working!"}

@app.get("/movies")
def list_movies(): 
    return get_movies()

@app.get("/recommend")
def recommend(movie_title: str):
    result = get_recommendations(movie_title)
    return {
        "status": "success",
        "movie_title": movie_title,
        "recommendations": result
    }
