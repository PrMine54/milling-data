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

app = FastAPI(title="CardioTwin",
              version="0.0.1")

model_name = "ECG DataBase Gradient Boost Classifier"
version = "v1.0.0"
MODEL_PATH = "gbc_deployment.pkl"
#MODEL_PATH = "knn_model.pkl"

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


# Input for data validation
class Input(BaseModel):
    Px: int = Field(..., gt=0)
    QT_ampl: int = Field(..., gt=0)
    ST_QS_ampl: int = Field(..., gt=0)
    Tx: int = Field(..., gt=0)
    Py: int = Field(..., gt=0)
    ST_time: int = Field(..., gt=0)
    ST_ampl: int = Field(..., gt=0)
    Sx: int = Field(..., gt=0)
    Sy: int = Field(..., gt=0)
    Ty: int = Field(..., gt=0)
    PT_ampl: int = Field(..., gt=0)
    Qx: int = Field(..., gt=0)
    Qy: int = Field(..., gt=0)
    ST_dist: int = Field(..., gt=0)
    QRS_angle: int = Field(..., gt=0)

    class Config:
        schema_extra = {'example': {'Px': 3,
                                    'QT_ampl': 3,
                                    'ST_QS_ampl': 1,
                                    'Tx': 2,
                                    'Py': 2,
                                    'ST_time': 2,
                                    'ST_ampl': 1,
                                    'Sx': 3,
                                    'Sy': 3,
                                    'Ty': 2,
                                    'PT_ampl': 4,
                                    'Qx': 2,
                                    'Qy': 2,
                                    'ST_dist': 2,
                                    'QRS_angle': 3}}


class Input2(BaseModel):
    time: str = Field(...)
    person_id: str = Field(...)
    predicted: str = Field(...)


# Ouput for data validation
class Output2(BaseModel):
    time: str
    person_id: str
    predicted: str


class Output(BaseModel):
    label: str
    prediction: int


@app.get('/info')
def model_info():
    """Return model information, version, how to call"""
    return {
        "name": model_name,
        "version": version
    }


@app.get('/health')
def service_health():
    """Return service health"""
    return {
        "ok"
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
