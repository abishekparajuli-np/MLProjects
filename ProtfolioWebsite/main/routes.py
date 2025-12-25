
from flask import render_template,url_for,flash,redirect,request,abort,jsonify
from main import app
from main.movie_recommendation import get_recommendations,MOVIES
@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/projects")
def projects():
    return render_template("projects.html")

@app.route("/movie-recommendation", methods=["GET", "POST"])
def movie_recommendation():
    recommendations = []

    if request.method == "POST":
        movie_name = request.form.get("movie_name")
        result = get_recommendations(movie_name)

        # Handle errors and recommendations
        if "error" in result:
            recommendations = [{"title": result["error"], "poster": "https://via.placeholder.com/500x750?text=No+Poster"}]
        else:
            recommendations = result["recommendations"]

    return render_template(
        "movie_recommendation.html",
        recommendations=recommendations,
        title="Movie Recommendation",
    )
@app.route("/search", methods=["GET"])
def search():
    query = request.args.get("query", "").strip().lower()
    if not query:
        return jsonify([])  # Return empty list for blank queries

    # Filter movies based on query
    matching_movies = MOVIES[MOVIES['title'].str.lower().str.contains(query, na=False)]
    suggestions = matching_movies['title'].head(10).tolist()  # Return top 10 matches
    return jsonify(suggestions)

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
