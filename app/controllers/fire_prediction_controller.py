from app.models.fire_prediction_model import database
from flask import jsonify, request

db = database()

def findAll():
    print("controller called1111")
    dbresult = list(db.findAll())
    print(dbresult)
    result = []

    for item in dbresult:
        print(item)
        print(item['temperature'])
        user = {
            # "id" : item['_id'],
            "temperature" : item['temperature'],
            "humidity" : item['humidity'],
            "time" : item['time'],
            "device_id" : item['device_id'],
            "wind_speed" : item['wind_speed'],
            "rain" : item['rain'],

        }
        result.append(user)
    print("result", result)

    return jsonify(result)