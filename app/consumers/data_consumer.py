import pika
from pika.exchange_type import ExchangeType
from app.prediction import fire_predictor
import json
from app.models.fire_prediction_model import  database

exchangeName = "pyropro"
firePredictionRoutingKey = "PyroproFirePredictionQueue"

db = database()

def on_message_received(ch, method, properties, body):
    print(f'Payments - received new message: {body}')
    # time.sleep(5)
    print("Wait is over.")
    data = json.loads(body)
    print(data)
    predictData = [data['temperature'], data['humidity'], data['wind_speed'], data['rain']]
    predValue = fire_predictor.prediction(predictData);

    print(predValue[0])
    if predValue[0] == 'fire':
        db.insert(data)



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
