import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

# OR, the same with increased verbosity
load_dotenv(verbose=True)

# OR, explicitly providing path to '.env'
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

IO_LINK_MASTER_URL = os.getenv("IO_LINK_MASTER_URL")
FLASK_SECRET_KEY = os.getenv("FLASK_SECRET_KEY")

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
