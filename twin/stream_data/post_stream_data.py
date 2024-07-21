import random
import time

import pandas as pd
import requests

URL = f"http://10.8.129.83:8000/cloud_predict"


def post_data(data):
    response = requests.post(URL, json=data)
    response.json()
    print(response.content)


def stream_test_data():
    df = pd.read_csv("test.csv").drop("label", axis=1)
    for i in range(len(df)):
        test_sample = df.iloc[i].to_dict()
        post_data(test_sample)
        time.sleep(random.randint(5, 120))


if __name__ == "__main__":
    stream_test_data()
