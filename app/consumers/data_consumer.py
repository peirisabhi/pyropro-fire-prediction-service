import pika
from pika.exchange_type import ExchangeType
import time

exchangeName = "pyropro"
firePredictionRoutingKey = "PyroproFirePredictionQueue"


def on_message_received(ch, method, properties, body):
    print(f'Payments - received new message: {body}')
    # time.sleep(5)
    print("Wait is over.")


def start_consume():
    connection_parameters = pika.ConnectionParameters('localhost')

    connection = pika.BlockingConnection(connection_parameters)

    channel = connection.channel()

    channel.exchange_declare(exchange=exchangeName, exchange_type=ExchangeType.direct, durable=True)

    queue = channel.queue_declare(queue=firePredictionRoutingKey, durable=True)

    channel.queue_bind(exchange=exchangeName, queue=queue.method.queue, routing_key=firePredictionRoutingKey)

    channel.basic_consume(queue=firePredictionRoutingKey, auto_ack=True,
                          on_message_callback=on_message_received)

    print('Payments Starting Consuming')
    channel.start_consuming()

# start_consume()
