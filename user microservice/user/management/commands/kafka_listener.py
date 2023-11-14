from django.core.management.base import BaseCommand
from confluent_kafka import Consumer, KafkaError
from user.message import process_user_message
from user.models import User
import json

class Command(BaseCommand):
    help = 'Listen to Kafka topic and process messages'

    def handle(self, *args, **options):
        conf = {
            'bootstrap.servers': "pkc-6ojv2.us-west4.gcp.confluent.cloud:9092",
            'security.protocol': "SASL_SSL",
            'sasl.username': "DTWX3U2LLHWUJAV2",
            'sasl.password': "TCdwZgOCrk9XGeNhqqqTNLd1snJciKTN3kMOXxaGHBFPfw/jQvZgbt5psGWoEnHD",
            'sasl.mechanism': "PLAIN",
            'group.id': "myGroup",
            'auto.offset.reset': 'earliest'
        }

        consumer = Consumer(conf)

        topic = 'default'
        consumer.subscribe([topic])

        while True:
            msg = consumer.poll(1.0)

            if msg is None:
                continue

            if msg.error():
                if msg.error().code() == KafkaError._PARTITION_EOF:
                    print(f'Reached end of partition {msg.topic()} [{msg.partition()}]')
                else:
                    print(f'Error while consuming message: {msg.error().str()}')
            else:
                key = msg.key()
                value = msg.value()

                if key == b'user_created':
                    process_user_message(key, value)
                    print(f'Received message - Key: {key}, Value: {value}')
                print(f'Key Error: {key}, Value: {value}')

        consumer.close()
