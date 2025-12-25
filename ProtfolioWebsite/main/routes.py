
from flask import render_template,url_for,flash,redirect,request,abort
from main import app
from main.movie_recommendation import get_recommendations,load_model
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
    recommendations = None
    if request.method == "POST":
        movie_name = request.form.get("movie_name")
        recommendations = get_recommendations(movie_name)
    return render_template(
        "movie_recommendation.html", 
        recommendations=recommendations, 
        title="Movie Recommendation"
    )

@app.route("/gallery")
def gallery():
    return render_template("gallery.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")
