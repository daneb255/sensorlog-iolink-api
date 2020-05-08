from flask import Flask
from iolink import get_sensor_data
from core.config import FLASK_SECRET_KEY

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY


@app.route("/sensor-data")
def get_data():
    data = get_sensor_data()
    return data


@app.route("/")
def default():
    return 'Sensor API'
