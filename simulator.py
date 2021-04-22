from datetime import datetime
import random
import json


def generate_data(database):
    label = "0"
    deviceID = "simulator"
    date_time = datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S.%f")

    x = str(round(random.random(), 6))
    y = str(round(random.random(), 6))
    z = str(round(random.random(), 6))

    data = {
        "database": database,
        "loggingTime": date_time,
        "deviceID": deviceID,
        "label": label,
        "motionUserAccelerationX": x,
        "motionUserAccelerationY": y,
        "motionUserAccelerationZ": z
    }

    return json.dumps(data)
