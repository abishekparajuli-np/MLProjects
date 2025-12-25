import os
import pickle
import requests

# Base directory and model path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "movie_recommendation.pkl")

# API key for TMDB
API_KEY = "8265bd1679663a7ea12ac168da84d2e8"

# Load data
with open(MODEL_PATH, "rb") as file:
    data = pickle.load(file)

MOVIES = data["movies"]              # pandas DataFrame
SIMILARITY_MATRIX = data["similarity"]

def fetch_poster(movie_id):
    """Fetch movie poster URL using The Movie Database API."""
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key={API_KEY}&language=en-US"
    response = requests.get(url)
    data = response.json()
    if "poster_path" in data and data["poster_path"]:
        return f"https://image.tmdb.org/t/p/w500{data['poster_path']}"
    return "https://via.placeholder.com/500x750?text=No+Poster+Available"

def get_recommendations(movie_name, top_n=5):
    """Get movie recommendations along with their posters."""
    if not movie_name:
        return {"error": "Please enter a movie name."}

    # Match the movie by title
    matched = MOVIES[MOVIES['title'].str.lower() == movie_name.lower()]
    if matched.empty:
        return {"error": "Movie not found. Please try again."}

    # Get the index of the matched movie
    movie_idx = matched.index[0]

    # Compute similarity scores and sort them
    scores = list(enumerate(SIMILARITY_MATRIX[movie_idx]))
    scores = sorted(scores, key=lambda x: x[1], reverse=True)

    # Fetch top recommendations
    recommendations = []
    for i, _ in scores[1:top_n + 1]:  # Skip the first (since it's the input movie)
        recommendation = {"title": MOVIES.iloc[i]['title']}
        recommendation["poster"] = fetch_poster(MOVIES.iloc[i]['movie_id'])
        recommendations.append(recommendation)

    return {"recommendations": recommendations}