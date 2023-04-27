from app.models.fire_prediction_model import database
from flask import jsonify, request

db = database()

def findAll():

    dbresult = db.findAll()
    result = []
    for items in dbresult:
        user = {
            "id" : items[0],
            "username" : items[1],
            "firstname" : items[2],
            "lastname" : items[3],
            "email" : items[4]
        }
        result.append(user)

    return jsonify(result)