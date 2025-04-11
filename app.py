from flask import Flask, jsonify
from flask_cors import CORS  # 👈 new
import requests
import os

app = Flask(__name__)
CORS(app)  # 👈 this enables CORS for all routes

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PLACE_ID = os.getenv("PLACE_ID")

@app.route('/')
def home():
    return "Google Reviews API is running"

@app.route('/reviews')
def get_reviews():
    url = (
        f"https://maps.googleapis.com/maps/api/place/details/json?"
        f"place_id={PLACE_ID}&fields=name,reviews,rating&key={GOOGLE_API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    return jsonify(data)
app.run(host='0.0.0.0', port=8080)
