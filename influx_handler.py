from influxdb import InfluxDBClient
from core.config import INFLUX_PASSWORD, INFLUX_USER, INFLUX_HOST, INFLUX_DB

client = InfluxDBClient(host=INFLUX_HOST, port=8086, username=INFLUX_USER, password=INFLUX_PASSWORD)

client.switch_database(INFLUX_DB)


def write_to_influx(timestamp, x, y, z, device_id, label):
    try:
        data = [
            {
                "measurement": "motionUserAcceleration",
                "tags": {
                    "device_id": device_id,
                    "label": label
                },
                "time": timestamp,
                "fields": {
                    "motionUserAccelerationX": x,
                    "motionUserAccelerationY": y,
                    "motionUserAccelerationZ": z
                }
            }
        ]

        #results = client.query('SELECT * FROM "iphone"."autogen"."motionUserAcceleration" WHERE time > now() - 4d')
        #print(results.raw)

        client.write_points(data)
        return True
    except Exception as e:
        print(e)
