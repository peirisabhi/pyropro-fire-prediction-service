from flask import Flask
import threading
import time

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"

def run_app():
    app.run(debug=False, threaded=True)

def while_function():
    i = 0
    while i < 20:
        time.sleep(1)
        print(i)
        i += 1

if __name__ == "__main__":
    first_thread = threading.Thread(target=run_app)
    second_thread = threading.Thread(target=while_function)
    first_thread.start()
    second_thread.start()