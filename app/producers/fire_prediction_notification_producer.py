import pika
from pika.exchange_type import ExchangeType

exchangeName = "pyropro"
routingKey = "PyroproFirePredictionQueue"

connection_parameters = pika.ConnectionParameters('localhost')

connection = pika.BlockingConnection(connection_parameters)

channel = connection.channel()

channel.exchange_declare(exchange=exchangeName, exchange_type=ExchangeType.direct)

message = 'This message needs to be routed1111'

channel.basic_publish(exchange=exchangeName, routing_key=routingKey, body=message)

print(f'sent message: {message}')

connection.close()