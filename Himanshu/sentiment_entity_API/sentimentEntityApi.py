from flask import Flask, request, jsonify
from model import Analysis

app = Flask(__name__)

# loading model
api = Analysis()


@app.route('/check', methods=['POST', 'GET'])
def check():

    text = request.form.get("text")

    try:
        value = api.model(text)
    except Exception as e:
        print("error occured", e)
        value = {}

    result_dict = {"Sentiment": value[0],
                   "Entities": value[1]
                   }

    return jsonify(result_dict)


if __name__ == "__main__":
    app.run(debug=True)
