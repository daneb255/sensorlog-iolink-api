import pika
import sys
import os
import json

from core.config import RABBITMQ_USER, RABBITMQ_VHOST, RABBITMQ_PASSWORD, RABBITMQ_HOST
from influx_handler import write_to_influx


def main():
    credentials = pika.PlainCredentials(RABBITMQ_USER, RABBITMQ_PASSWORD)
    connection = pika.BlockingConnection(pika.ConnectionParameters(RABBITMQ_HOST, 5672, RABBITMQ_VHOST,
                                                                   credentials))
    channel = connection.channel()

    channel.queue_declare(queue='sensor-data')

    def callback(ch, method, properties, body):
        data = json.loads(body.decode('utf-8'))
        try:
            write_to_influx(data['loggingTime'], data['motionUserAccelerationX'], data['motionUserAccelerationY'],
                            data['motionUserAccelerationZ'], data['deviceID'], data['label'])
        except Exception as e:
            print(e)
        print("[x] Received %r" % body)

    channel.basic_consume(queue='sensor-data', on_message_callback=callback, auto_ack=True)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
