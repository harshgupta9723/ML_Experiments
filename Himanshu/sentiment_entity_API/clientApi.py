import requests
import json


def run(text):
    result = requests.get("http://127.0.0.1:5000/check", data={"text": text})
    json_data = json.loads(result.text)
    print(json_data)


# run("Apple is looking at buying U.K. startup for $1 billion")
run("Bill Gates and Elon Musk they both are the very telented persons")
