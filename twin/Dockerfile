# Base image
FROM python:3.8

# Set working directory
WORKDIR /app


COPY requirements.txt /app
COPY gbc_deployment.pkl /app
COPY api.py /app
COPY kafka_client.py /app

# Install dependencies
RUN pip install -r requirements.txt


# Run the application
EXPOSE 8000
CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port",   "8000"]