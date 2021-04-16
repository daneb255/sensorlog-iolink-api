import pika
from core.config import RABBITMQ_USER, RABBITMQ_VHOST, RABBITMQ_PASSWORD, RABBITMQ_HOST


def rabbit_producer(data):
    try:
        credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
        connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, 5672, RABBITMQ_VHOST,
                                                                       credentials))
        channel = connection.channel()

        channel.queue_declare(queue='sensor-data')

        channel.basic_publish(exchange='',
                              routing_key='sensor-data',
                              body=data)
        connection.close()
        return True
    except Exception as e:
        print(e)
        return False
