import pickle
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "model", "movie_recommendation.pkl")

with open(MODEL_PATH, "rb") as f:
    data = pickle.load(f)

print(type(data))
print(data)
