from flask import Flask, jsonify
import requests
import os

app = Flask(__name__)

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
PLACE_ID = os.getenv("PLACE_ID")

@app.route('/')
def index():
    return "Google Reviews API is running. Go to /reviews to see reviews."

@app.route('/reviews')
def get_reviews():
    url = (
        f"https://maps.googleapis.com/maps/api/place/details/json?"
        f"place_id={PLACE_ID}&fields=reviews&key={GOOGLE_API_KEY}"
    )
    response = requests.get(url)
    data = response.json()
    reviews = data.get("result", {}).get("reviews", [])
    return jsonify(reviews)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
