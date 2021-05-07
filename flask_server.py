from flask import Flask, request, jsonify
from iolink import get_sensor_data
from core.config import FLASK_SECRET_KEY
from rabbit_producer import rabbit_producer
from simulator import generate_data

app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY


@app.route('/sensor-data', methods=['GET', 'POST'])
def get_data():
    data = get_sensor_data()
    return data


@app.route('/simulator/<database>', methods=['GET'])
def simulator(database):
    data = generate_data(database)
    if rabbit_producer(data):
        return jsonify(success=True)
    else:
        return jsonify(success=False, database=database, data=data)


@app.route('/mobile-data', methods=['GET', 'POST'])
def parse_request():
    print(request.json)
    data = request.data
    data['database'] = 'influxdb'
    if rabbit_producer(data):
        return jsonify(success=True)
    else:
        return jsonify(success=False)


@app.route("/")
def default():
    return 'Sensor API'


if __name__ == "__main__":
    app.run(host='0.0.0.0')
