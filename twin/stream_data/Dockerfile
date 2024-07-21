# Base image
FROM python:3.8

# Set working directory
WORKDIR /stream


COPY requirements.txt /stream
COPY post_stream_data.py /stream
COPY test.csv /stream

# Install dependencies
RUN pip install -r requirements.txt


# Run the application

CMD ["python", "post_stream_data.py"]
