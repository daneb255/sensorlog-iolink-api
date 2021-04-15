import requests
from core.config import IO_LINK_MASTER_URL, SENSORS


def get_sensor_data():
    try:
        for k, sensor in SENSORS.items():
            url = '{}/iolinkmaster/port[{}]/iolinkdevice/pdin/getdata'.format(IO_LINK_MASTER_URL, sensor["port"])
            r = requests.get(url)
            if r.json()['code'] == 200:
                print('Successfully get value from Port {} | Sensor {}!'.format(k, sensor["id"]))
                value = sensor_data_conversion(sensor["id"], r.json()['data']['value'])

                # update json
                sensor["value"] = value

                print('Value: {} {}'.format(value, sensor["unit"]))
            else:
                print('Cannot get value from port {} !'.format(sensor["id"]))
                # update json
                sensor["value"] = 0

        return SENSORS

    except Exception as e:
        print(e)
        return SENSORS


def sensor_data_conversion(sensor_id, sensor_value):
    result = ''
    if sensor_id == 'O5D100':
        result = (int(sensor_value, 16) >> 4) * 1.0 + 0
    elif sensor_id == 'TN2415':
        result = (int(sensor_value, 16) >> 2) / 10

    return result
