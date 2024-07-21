import numpy as np
import gradio as gr
import pickle
import joblib

MODEL_PATH = "knn_model.pkl"
SCALER_PATH = "scaler_model.pkl"

model = pickle.load(open(MODEL_PATH, 'rb'))
#scaler = joblib.load(SCALER_PATH)


def predict(input1: float,
            input2: float,
            input3: float,
            input4: float,
            input5: float):
    input_data = np.array([[input1, input2, input3, input4, input5]])
    prediction = model.predict(input_data)
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
    title="K-NN Binary Classification",
    description="Enter five features to get a binary classification result through K-NN Binary Classification model."
)

iface.launch()