import os
import pickle
import uuid
from datetime import datetime

import pandas as pd
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from prometheus_fastapi_instrumentator import Instrumentator
from pydantic import BaseModel, Field

from kafka_client import KafkaClient

app = FastAPI(title="K-Nearest Neighbours")

model_name = "K-Nearest Neighbours Classifier"

MODEL_PATH = "knn_model.pkl"

model = pickle.load(open(MODEL_PATH, 'rb'))

client = KafkaClient()
TOPIC_stream = f"{os.getenv('TOPIC')}"
TOPIC_edge = f"{os.getenv('TOPIC_EDGE')}"

def get_uuid():
    return str(uuid.uuid4())

def predict(x):
    prediction = model.predict(x)[0]
    return prediction

def get_model_response(input_data):
    x = pd.json_normalize(input_data.__dict__)
    prediction = predict(x)

    label = "Faulty" if prediction == 1 else "Healthy"
    input_d = eval(input_data.json())
    input_d["time"] = datetime.now().__str__()
    input_d["person_id"] = f'Person_{get_uuid()}'
    input_d["predicted"] = label
    client.send_message(input_d, topic=TOPIC_stream)

    return {
        'label': label,
        'prediction': int(prediction)
    }

class Input(BaseModel):
    Parameter1: float = Field(..., gt=-1, lt=1)
    Parameter2: float = Field(..., gt=-1, lt=1)
    Parameter3: float = Field(..., gt=-1, lt=1)
    Parameter4: float = Field(..., gt=-1, lt=1)
    Parameter5: float = Field(..., gt=-1, lt=1)

    class Config:
        schema_extra = {'example': {'Parameter1': -0.6,
                                    'Parameter2': 0.7,
                                    'Parameter3': 0.1,
                                    'Parameter4': 0,
                                    'Parameter5': 0.9}}

class Input2(BaseModel):
    time: str = Field(...)
    person_id: str = Field(...)
    predicted: str = Field(...)

class Output2(BaseModel):
    time: str
    person_id: str
    predicted: str


class Output(BaseModel):
    label: str
    prediction: int

@app.get('/')
def intro():
    return {
        "introduction": "Hello, 'Person_" + get_uuid()
    }

@app.get('/info')
def model_info():
    """Return model information, version, how to call"""
    return {
        "name": model_name
    }

@app.get('/health')
def service_health():
    """Return service health"""
    return {
        "ok"
    }

@app.get('/prediction')
def intro():
    return {
        "introduction": "Hello, 'Person_" + get_uuid()
    }

@app.post('/edge_result', response_model=Output2,
          summary="Edge'den gelen test sonuclari bu api üzerinden kafka'ya basilir")
def edge_predict_res(input: Input2):
    data = input.__dict__
    client.send_message(data, topic=TOPIC_edge)
    return data


@app.post('/cloud_predict', response_model=Output)
def model_predict(input: Input):
    """Predict with input"""
    response = get_model_response(input)
    return response


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Instrumentator().instrument(app).expose(app)