import json
from colorama import init, Fore, Style
import requests
import os
from dotenv import load_dotenv

# Load token from the .env file
load_dotenv()
TMDB_API_KEY = os.getenv("TMDB_API_KEY")
HEADERS = {"Authorization": f"Bearer {TMDB_API_KEY}","accept": "application/json" }


def fetch_movie(category: str, title: str) -> None:
    """

    function to fetch movies list by its category

    Args:
        category (str): category of the movie
        title (str): title of the movie category

    """
    url = f"https://api.themoviedb.org/3/movie/{category}?language=en-US&page=1"
    try:
        response = requests.get(url, headers=HEADERS)
        print(f"{Fore.YELLOW}{title} Movies:")
        print(f"{Fore.YELLOW}--------------------------------------------------------------------------------------------------")
        for movie in response.json()["results"]:
            print(f"{Fore.GREEN}Title: {Fore.YELLOW}{movie['title']}")
            print(f"{Fore.GREEN}Rating: {Fore.WHITE}{movie['vote_average']}")
            print(f"{Fore.GREEN}Released: {Fore.WHITE}{movie['release_date']}")
            print(f"{Fore.GREEN}Overview: {Fore.WHITE}{movie['overview']}")
            print(f"{Fore.YELLOW}--------------------------------------------------------------------------------------------------")

    except requests.exceptions.RequestException as e:
        print(f"{Fore.RED}ERROR FETCHING DATA: {Fore.LIGHTRED_EX}{e}")
    except json.decoder.JSONDecodeError as e:
        print(f"{Fore.RED}ERROR DECODING API RESPONSE: {Fore.LIGHTRED_EX}{e}")


def get_now_playing() -> None:
    """Get the now playing movies from TMDB API"""
    fetch_movie("now_playing", "Now Playing Movies")

def get_popular() -> None:
    """Get popular movies from TMDB API"""
    fetch_movie("popular", "Popular Movies")

def get_top_rated() -> None:
    """Get top-rated movies from TMDB API"""
    fetch_movie("top_rated", "Top Rated Movies")

def get_upcoming() -> None:
    """Get upcoming movies from TMDB API"""
    fetch_movie("upcoming", "Upcoming Movies")