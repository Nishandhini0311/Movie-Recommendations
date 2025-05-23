import requests

def get_poster_url(title):
    api_key = "YOUR_IMDB_API_KEY"
    url = f"https://api.themoviedb.org/3/search/movie?api_key={api_key}&query={title}"
    response = requests.get(url).json()
    poster_path = response['results'][0]['poster_path']
    return f"https://image.tmdb.org/t/p/w500/{poster_path}"
