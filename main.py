# from flask import Flask
from app.models.fire_prediction_model import database as db

# app = Flask(__name__)
#
#
# # @app.route('/')
# # def hello_world():  # put application's code here
# #     mydict = {"name": "John", "address": "Highway 37"}
# #     db.insert(mydict)
# #     return "asasas"
#
# if __name__ == '__main__':
#     db = db()
#     app.run(debug=True)



from app import app
# from threading import Thread
from app.consumers import data_consumer
# import multiprocessing
# import time
#
# if __name__ == "__main__":
#
#     # app.run(debug=True)
#     # p = multiprocessing.Process(data_consumer.start_consume())
#     # p.start()
#
#     thread1 = Thread(data_consumer.start_consume())
#     thread1.start()
#
#     thread2 = Thread(app.run(debug=True))
#     thread2.start()
#
#     print("asasa")

# def API():
#    print('In API selction')
#    app.run(debug=True)
#
# if __name__ == "__main__":
#    config = {"Something":"SomethingElese"}
#    p = multiprocessing.Process(target=API)
#    p.start()
#    time.sleep(3)
#    print('After Flask run')


# from flask import Flask
import threading
import time

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#     return "Hello, World!"

def run_app():
    app.run(debug=False, threaded=True)

def while_function():
    data_consumer.start_consume()

if __name__ == "__main__":
    first_thread = threading.Thread(target=run_app)
    second_thread = threading.Thread(target=while_function)
    first_thread.start()
    second_thread.start()
