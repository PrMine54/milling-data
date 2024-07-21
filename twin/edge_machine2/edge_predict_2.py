import pickle
import random
import time
import uuid

import pandas as pd
import requests

# Create a metric to track time spent and requests made.
model = pickle.load(open("gbc_deployment.pkl", 'rb'))
URL = f"http://10.8.129.83:8000/edge_result"


def post_data(data):
    response = requests.post(URL, json=data)
    response.json()
    print(response.content)


def get_uuid():
    return str(uuid.uuid4())


def predict(x):
    prediction = model.predict(x)[0]
    return prediction


def stream_test_data():
    df = pd.read_csv("test.csv").drop("label", axis=1)
    for i in range(len(df)):
        test_sample = df.iloc[i].to_dict()
        predict_request(test_sample)
        time.sleep(random.randint(5, 120))


def predict_request(input_data):
    x = pd.json_normalize(input_data)
    prediction = predict(x)
    label = "Hasta" if prediction == 1 else "Saglikli"
    m = {"time": pd.datetime.now().__str__(),
         "person_id": f'Person_{get_uuid()}',
         "predicted": label}
    post_data(m)
    return m


if __name__ == '__main__':
    stream_test_data()
