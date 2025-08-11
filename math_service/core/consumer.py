import os

import pika
import json

from dotenv import load_dotenv

# loading .env variables
load_dotenv()

# loading amqp url from .env
AMQP_URL = os.getenv("CLOUDAMQP_URL")


params = pika.URLParameters(AMQP_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.queue_declare(queue='math_logs', durable=True)

def callback(ch, method, properties, body):
    data = json.loads(body)
    print(f" Message received: {data}")

channel.basic_consume(queue='math_logs', on_message_callback=callback, auto_ack=True)

print(" Waiting for messages...")
channel.start_consuming()
