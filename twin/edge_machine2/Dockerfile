# Base image
FROM python:3.8

# Set working directory
WORKDIR /edge2


COPY requirements.txt /edge2
COPY edge_predict_2.py /edge2
COPY test.csv /edge2
COPY gbc_deployment.pkl /edge2

# Install dependencies
RUN pip install -r requirements.txt


# Run the application
CMD ["python", "edge_predict_2.py"]
