from flask import Flask

app = Flask(__name__)

from app.routes.fire_prediction_route import *
#
app.register_blueprint(blueprint=fire_prediction_blueprint)
