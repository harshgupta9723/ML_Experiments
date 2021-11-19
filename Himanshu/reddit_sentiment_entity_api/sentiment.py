from flask import Flask, request, jsonify
from model import Models

app = Flask(__name__)

# loading model
api = Models()


@app.route('/sentiment', methods=['POST', 'GET'])
def check():

    text = request.form.get("text")

    try:
        value = api.sentiment(text)
    except Exception as e:
        print("error occured", e)
        value = {}

    result_dict = {"Sentiment": value}

    return jsonify(result_dict)


if __name__ == "__main__":
    app.run(debug=True)
