import requests

API_KEY = "xxx"
URL = "xxx"


def emotion_detector(text):
    """
    Calls IBM Watson NLU and returns emotion scores.
    Includes error handling for status code 400 and API failures.
    """

    # -------------------------
    # Input validation (Task 7A)
    # -------------------------
    if text is None or text.strip() == "":
        return {
            "anger": None,
            "disgust": None,
            "fear": None,
            "joy": None,
            "sadness": None,
            "error": "400 - Invalid input text"
        }

    endpoint = f"{URL}/v1/analyze?version=2022-04-07"

    payload = {
        "text": text,
        "features": {
            "emotion": {}
        }
    }

    try:
        response = requests.post(
            endpoint,
            auth=("apikey", API_KEY),
            headers={"Content-Type": "application/json"},
            json=payload,
            timeout=10
        )

        # -------------------------
        # Handle HTTP errors
        # -------------------------
        if response.status_code != 200:
            return {
                "anger": None,
                "disgust": None,
                "fear": None,
                "joy": None,
                "sadness": None,
                "error": f"HTTP {response.status_code}",
                "details": response.text
            }

        data = response.json()

        emotions = data.get("emotion", {}).get("document", {}).get("emotion", {})

        return {
            "anger": emotions.get("anger", 0),
            "disgust": emotions.get("disgust", 0),
            "fear": emotions.get("fear", 0),
            "joy": emotions.get("joy", 0),
            "sadness": emotions.get("sadness", 0)
        }

    except requests.exceptions.Timeout:
        return {
            "error": "Request timeout"
        }

    except requests.exceptions.ConnectionError:
        return {
            "error": "Connection error"
        }

    except Exception as e:
        return {
            "error": str(e)
        }
