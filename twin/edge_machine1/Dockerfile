# Base image
FROM python:3.8

# Set working directory
WORKDIR /edge1


COPY requirements.txt /edge1
COPY edge_predict_1.py /edge1
COPY test.csv /edge1
COPY gbc_deployment.pkl /edge1

# Install dependencies
RUN pip install -r requirements.txt

EXPOSE 8000
# Run the application
CMD ["python", "edge_predict_1.py"]
