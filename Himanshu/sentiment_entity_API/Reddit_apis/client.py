import requests
import json
import time
import pandas as pd

data = pd.read_csv(
    "/home/himanshu/Desktop/sentiment_analysis_entity/amazon_indeed_review.csv")


desc = data['description'][:1000]


def sentiment(text):
    t = []
    for i in range(len(text)):
        start_time = time.time()

        result = requests.get(
            "http://127.0.0.1:5000/sentiment", data={"text": text[i]})

        end_time = time.time()
        t.append(end_time - start_time)

        json_data = json.loads(result.text)
        print(json_data)

    print(sum(t))


def entity(text):
    t = []
    for i in range(len(text)):
        start_time = time.time()

        result = requests.get(
            "http://127.0.0.1:5000/entity", data={"text": text[i]})

        end_time = time.time()
        t.append(end_time - start_time)

        json_data = json.loads(result.text)
        print(json_data)

    print(sum(t))


# run("Apple is looking at buying U.K. startup for $1 billion")

entity(desc)
