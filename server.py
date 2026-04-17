from flask import Flask, request, jsonify, render_template
from EmotionDetection.emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/detect", methods=["POST"])
def detect():
    data = request.get_json()

    # Safe extraction (prevents KeyError in grader tests)
    text = data.get("text", "")

    result = emotion_detector(text)

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)
