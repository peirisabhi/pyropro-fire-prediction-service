from app import app
from app.controllers import fire_prediction_controller
from flask import Blueprint, request

fire_prediction_blueprint = Blueprint("fire_prediction_router", __name__)


@app.route("/users", methods=["GET"])
def findAll():
    return fire_prediction_controller.findAll()
