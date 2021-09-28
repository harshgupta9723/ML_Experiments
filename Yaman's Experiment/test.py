from flask import Flask, request, jsonify
import pandas as pd
import pyarrow as pa
import redis
import requests
import json
import time


def read_data():
    data = pd.read_csv("scoring_data.csv")

    df = pd.DataFrame({
        'job_id': data['job_id'],
        "key": data["key"],
        "percentage": data["percentage"]
    })
    df.set_index('job_id', inplace=True)
    return df


def redis_conn(df):
    r = redis.Redis(host='localhost', port=6379, db=0)

    context = pa.default_serialization_context()
    r.set("key", context.serialize(df).to_buffer().to_pybytes())
    redis_data = context.deserialize(r.get("key"))
    return redis_data


def main(job_id):
    start_time = time.time()
    link = "http://143.198.118.108:5080/jobs"
    result = requests.post(link, data={'job_id': job_id})
    json_data = json.loads(result.text)

    df = read_data()
    redis_data = redis_conn(df)
    dic = {'key': [], 'percentage': []}
    for key, value in json_data['recommended_jobs'].items():
        try:
            if redis_data.iloc[value['job_id']]['percentage'] >= 36:
                dic['key'].append(redis_data.iloc[value['job_id']]['key'])
                dic['percentage'].append(
                    redis_data.iloc[value['job_id']]['percentage'])
        except Exception:
            pass

    res_df = pd.DataFrame(dic)
    res_df.set_index('key', inplace=True)
    result = res_df.to_json(orient='index')
    value = json.loads(result)
    end_time = time.time()
    print(end_time-start_time)
    return value


app = Flask(__name__)


@app.route('/scored_jobs', methods=['POST', 'GET'])
def scored_jobs():

    job_id = request.form.get("job_id")

    value = main(job_id)

    result_dict = {"recommended_jobs": value}

    return jsonify(result_dict)


if __name__ == '__main__':
    app.run(debug=True)
