from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def index():
    time.sleep(59)  # sleep 59 seconds
    return "Hello, OpenShift!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
