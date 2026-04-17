import requests

BASE_URL = "http://127.0.0.1:5000/detect"

test_cases = [
    "I am very happy today",
    "I feel sad and disappointed",
    "I am extremely angry",
    "I am scared of exams",
    "This is disgusting"
]

print("\n===== UNIT TESTING =====\n")

for i, text in enumerate(test_cases, 1):
    response = requests.post(BASE_URL, json={"text": text})

    print(f"Test {i}: {text}")
    print(response.json())
    print("-" * 40)
