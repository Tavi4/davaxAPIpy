import pika
import os
from dotenv import load_dotenv
import json

# loading .env variables
load_dotenv()

# loading amqp url from .env
AMQP_URL = os.getenv("CLOUDAMQP_URL")

if not AMQP_URL:
    raise RuntimeError("CLOUDAMQP_URL is not set. Please check your .env file.")

params = pika.URLParameters(AMQP_URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()
channel.queue_declare(queue='math_logs', durable=True)

def publish_message(operation: str, input_data: dict, result):
    message = {
        "operation": operation,
        "input": input_data,
        "result": result
    }

    channel.basic_publish(
        exchange='',
        routing_key='math_logs',
        body=json.dumps(message),
        properties=pika.BasicProperties(delivery_mode=2)
    )
