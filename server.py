from flask import Blueprint, render_template, request, jsonify
import requests

detect_emotion_blueprint = Blueprint("detect", __name__)

API_KEY = "_6HRCzk4lEMhIs202t5MNSw7vygd_AKlgZ8YEklhQAka"
URL = "https://api.au-syd.natural-language-understanding.watson.cloud.ibm.com/instances/967245b1-1bca-486d-98ad-8731701d954a"


def detect_emotion(text):
    endpoint = f"{URL}/v1/analyze?version=2022-04-07"

    response = requests.post(
        endpoint,
        auth=("apikey", API_KEY),
        headers={"Content-Type": "application/json"},
        json={
            "text": text,
            "features": {"emotion": {}}
        }
    )

    data = response.json()

    return data.get("emotion", {}).get("document", {}).get("emotion", {})


@detect_emotion_blueprint.route("/")
def home():
    return render_template("index.html")


@detect_emotion_blueprint.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()
    text = data.get("text", "")

    result = detect_emotion(text)

    return jsonify(result)
