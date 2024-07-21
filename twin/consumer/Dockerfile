# Base image
FROM python:3.8

# Set working directory
WORKDIR /app2


COPY requirements.txt /app2
COPY consumer.py /app2

# Install dependencies
RUN pip install -r requirements.txt


# Run the application
CMD ["python", "consumer.py"]