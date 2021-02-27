# iolink-sensor-api

## Start Dev-Server

### Windows
- `set FLASK_APP=flask_server.py`
- `set FLASK_ENV=development`
- `flask run`

### Linux
- `FLASK_APP=flask_server.py FLASK_ENV=development flask run`

## Start Prod-Server
- `python server.py`

## Helm chart
- `cd helm`
- `helm install -n sensorlog sensorlog . --set "connections.influx.user=REPLACE" --set "connections.influx.password=REPLACE" --set "connections.rabbitmq.user=REPLACE" --set "connections.rabbitmq.password=REPLACE"`

## Docker services

### producer & api
[Dockerhub - sensorlog-api](https://hub.docker.com/repository/docker/dbitzer/sensorlog-api)

### consumer
[Dockerhub - sensorlog-consumer](https://hub.docker.com/repository/docker/dbitzer/sensorlog-consumer)

### rabbitmq
[Dockerhub - rabbitmq](https://hub.docker.com/_/rabbitmq/)

### influxdb
[Dockerhub - influxdb](https://hub.docker.com/_/influxdb)

## Credits
Thanks to Dr. Bernd Thomas for SensoorLog iOS Application

[Sensorlog iOS App](http://sensorlog.berndthomas.net/)

[App Store - Sensorlog download](https://apps.apple.com/us/app/sensorlog/id388014573)
