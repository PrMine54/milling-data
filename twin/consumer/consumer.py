import io
import json
import os

import avro.schema as shema
import avro.io as aio
from kafka import KafkaConsumer

SCHEMA = shema.Parse(json.dumps(
    {
        'namespace': 'cardio.twin.avro',
        'type': 'record',
        'name': 'CARDIO_TWIN_PREDICTION',
        'fields': [
            {'name': 'person_id', 'type': ["string", "null"]},
            {'name': 'predicted', 'type': ["string", "null"]},
            {'name': 'Px', 'type': ["int", "null"]},
            {'name': 'QT_ampl', 'type': ["int", "null"]},
            {'name': 'ST_QS_ampl', 'type': ["int", "null"]},
            {'name': 'Tx', 'type': ["int", "null"]},
            {'name': 'Py', 'type': ["int", "null"]},
            {'name': 'ST_time', 'type': ["int", "null"]},
            {'name': 'ST_ampl', 'type': ["int", "null"]},
            {'name': 'Sx', 'type': ["int", "null"]},
            {'name': 'Sy', 'type': ["int", "null"]},
            {'name': 'Ty', 'type': ["int", "null"]},
            {'name': 'PT_ampl', 'type': ["int", "null"]},
            {'name': 'Qx', 'type': ["int", "null"]},
            {'name': 'Qy', 'type': ["int", "null"]},
            {'name': 'ST_dist', 'type': ["int", "null"]},
            {'name': 'QRS_angle', 'type': ["int", "null"]},
            {'name': 'time', 'type': ["string", "null"]}
        ]
    }))
KAFKA_URL = f"{os.getenv('INTERNAL_KAFKA_ADDR')}"
TOPIC = f"{os.getenv('TOPIC')}"
CONSUMER = KafkaConsumer(TOPIC,
                         bootstrap_servers=[KAFKA_URL])

for msg in CONSUMER:
    bytes_reader = io.BytesIO(msg.value)
    decoder = aio.BinaryDecoder(bytes_reader)
    reader = aio.DatumReader(SCHEMA)
    user1 = reader.read(decoder)
    print(user1)
