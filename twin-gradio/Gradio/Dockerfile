FROM python:3.11

WORKDIR /gradio_app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY requirements.txt /gradio_app
COPY knn_model.pkl /gradio_app
COPY scaler_model.pkl /gradio_app

EXPOSE 7860
CMD ["python", "gradio_app.py"]