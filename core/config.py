import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

IO_LINK_MASTER_URL = os.environ.get("IO_LINK_MASTER_URL", 'CHANGEME')
FLASK_SECRET_KEY = os.environ.get("FLASK_SECRET_KEY", 'CHANGEME')

INFLUX_USER = os.environ.get("INFLUX_USER", "CHANGEME")
INFLUX_PASSWORD = os.environ.get("INFLUX_PASSWORD", "CHANGEME")
INFLUX_HOST = os.environ.get("INFLUX_HOST", "influxdb")

RABBITMQ_HOST = os.environ.get("RABBITMQ_HOST", "rabbitmq")
RABBITMQ_USER = os.environ.get("RABBITMQ_USER", "CHANGEME")
RABBITMQ_PASSWORD = os.environ.get("RABBITMQ_PASSWORD", "CHANGEME")
RABBITMQ_VHOST = os.environ.get("RABBITMQ_VHOST", "sensordata")

SENSORS = {
    "1": {
        "id": "O5D100",
        "type": "distance sensor",
        "port": 1,
        "unit": "cm"
    },
    "2": {
        "id": "TN2415",
        "type": "temperature sensor",
        "port": 2,
        "unit": '{}C'.format(chr(176))
    }
}
