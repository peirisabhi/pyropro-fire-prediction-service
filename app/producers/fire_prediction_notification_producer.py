import pika
from pika.exchange_type import ExchangeType

exchangeName = "pyropro"
routingKey = "PyroproNotificationQueue"




def produce_message_to_notification(data):
    connection_parameters = pika.ConnectionParameters('localhost')

    connection = pika.BlockingConnection(connection_parameters)

    channel = connection.channel()

    channel.exchange_declare(exchange=exchangeName, exchange_type=ExchangeType.direct, durable=True)

    message = 'This message needs to be routed1111'

    channel.basic_publish(exchange=exchangeName, routing_key=routingKey, body=data)

    print(f'sent message: {data}')

    connection.close()