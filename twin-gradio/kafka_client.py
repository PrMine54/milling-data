import os
from json import dumps

from kafka import KafkaProducer

KAFKA_URL = f"{os.getenv('INTERNAL_KAFKA_ADDR')}"


class KafkaClient:
    TIMEOUT_OF_FLUSH = 30
    TIMEOUT_OF_CLOSE = 60
    TIMEOUT_OF_REQUEST = 60 * 1000

    def __init__(self):
        self.producer = KafkaProducer(bootstrap_servers=KAFKA_URL, compression_type='gzip',
                                      api_version=(0, 10, 1),
                                      value_serializer=lambda x: dumps(x).encode('utf-8'))

    def send_message(self, message, topic):
        self.producer.send(topic, message)

    def flush(self):
        self.producer.flush(self.TIMEOUT_OF_FLUSH)

    def close(self):
        self.producer.close(self.TIMEOUT_OF_CLOSE)
