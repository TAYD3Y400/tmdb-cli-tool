import requests
import os
from dotenv import load_dotenv

# Load token from the .env file
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
HEADERS = {"Authorization": f"Bearer {TMDB_API_KEY}","accept": "application/json" }


def fetch_movie(category: str, title: str) -> None:
    """fetch the movies list"""
    url = f"https://api.themoviedb.org/3/movie/{category}?language=en-US&page=1"
    try:
        response = requests.get(url, headers=HEADERS)
        print(f"{title} Movies:")
        print("")
        for movie in response.json()["results"]:
            print(f"Title: {movie['title']}")
            print(f"Rating: {movie['vote_average']}")
            print(f"Released: {movie['release_date']}")
            print(f"Overview: {movie['overview']}")
            print("")

    except requests.exceptions.RequestException as e:
        print(e)


def get_now_playing():
    """Get the now playing movies from TMDB API"""
    fetch_movie("now_playing", "Now Playing Movies")

def get_popular():
    """Get popular movies from TMDB API"""
    fetch_movie("popular", "Popular Movies")

def get_top_rated():
    """Get top-rated movies from TMDB API"""
    fetch_movie("top_rated", "Top Rated Movies")

def get_upcoming():
    """Get upcoming movies from TMDB API"""
    fetch_movie("upcoming", "Upcoming Movies")