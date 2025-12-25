import pickle

# Load Pretrained Model
def load_model():
    model_path = "model/movie_recommendation.pkl"
    with open(model_path, "rb") as file:
        movies, similarity_matrix = pickle.load(file)
    return movies, similarity_matrix

# Get Recommendations
def get_recommendations(movie_name):
    movies, similarity_matrix = load_model()
    try:
        movie_idx = movies.loc[movies['title'].str.lower() == movie_name.lower()].index[0]
        similarity_scores = list(enumerate(similarity_matrix[movie_idx]))
        sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
        recommended_movies = [movies['title'][item[0]] for item in sorted_scores[1:6]]
        return recommended_movies
    except Exception as e:
        print(f"Error: {e}")
        return ["Movie not found. Please try again."]