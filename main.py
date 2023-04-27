from flask import Flask
from app.models.fire_prediction_model import database as db

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    mydict = {"name": "John", "address": "Highway 37"}
    db.insert(mydict)
    return "asasas"

if __name__ == '__main__':
    db = db()
    app.run(debug=True)
