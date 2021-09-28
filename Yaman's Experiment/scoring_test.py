import pandas as pd
import numpy as np
import requests
import json


df = pd.read_csv('user.csv', index_col='job_id')

neg = np.random.randint(11, size=len(df))
df['negative'] = neg

pos = np.random.randint(11, size=len(df))
df['positive'] = pos

df.drop(columns=['userfeedback'], inplace=True)

df['total_reviews'] = df['negative']+df['positive']
df['percentage'] = df['positive']/df['total_reviews']*100

link = "http://143.198.118.108:5080/jobs"
result = requests.post(link, data={'job_id': 5})
json_data = json.loads(result.text)

df_percentage = df[['key', 'positive', 'negative', 'percentage']]

for key, value in json_data['recommended_jobs'].items():
    try:
        if df_percentage.iloc[value['job_id']]['percentage'] >= 36:
            print(df_percentage.iloc[value['job_id']])
    except Exception:
        pass
