import urllib.parse
from pymongo import MongoClient
from core.config import MONGODB_DB, MONGODB_HOST, MONGODB_USER, MONGODB_PASSWORD


def write_to_mongo(timestamp, x, y, z, device_id, label):
    try:
        username = urllib.parse.quote_plus(MONGODB_USER)
        password = urllib.parse.quote_plus(MONGODB_PASSWORD)
        client = MongoClient(f'mongodb://{username}:{password}@{MONGODB_HOST}')
        db = client[MONGODB_DB]
        col = db["motionUserAcceleration"]
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

        col.insert_one(data)
        return True
    except Exception as e:
        print(e)
