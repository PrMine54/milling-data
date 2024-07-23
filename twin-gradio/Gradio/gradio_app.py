import numpy as np
import gradio as gr
import pickle
from pymongo import MongoClient

MODEL_PATH = "knn_model.pkl"

model = pickle.load(open(MODEL_PATH, 'rb'))

mongo_client = MongoClient()
mongo_client = MongoClient("mongodb://admin:password@10.8.129.8:27017/")

db = mongo_client['mydatabase']
prediction_table = db['predictions']


def predict(input1: float,
            input2: float,
            input3: float,
            input4: float,
            input5: float):
    input_data = np.array([[input1, input2, input3, input4, input5]])
    prediction = model.predict(input_data)
    records = {
        'vib_spindle__quantile__q_0.7': input1,
        'vib_spindle__quantile__q_0.6': input2,
        'vib_spindle__fft_coefficient__attr_"abs"__coeff_0': input3,
        'vib_spindle__fft_coefficient__attr_"real"__coeff_0': input4,
        'vib_spindle__quantile__q_0.8': input5,
        'prediction': prediction
    }
    records = db.prediction_table.insert(records)
    return "Faulty" if prediction[0] == 1 else "Healthy"


iface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Feature 1"),
        gr.Number(label="Feature 2"),
        gr.Number(label="Feature 3"),
        gr.Number(label="Feature 4"),
        gr.Number(label="Feature 5")
    ],
    outputs="text",
    title="CNC Machine Predictive Maintenance",
    description="Enter five features to get a binary classification result through K-NN Binary Classification model."
)

iface.launch(server_name="0.0.0.0", server_port=8000)