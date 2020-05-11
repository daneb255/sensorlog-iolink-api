#!/bin/bash

cd /root/projects/iolink-sensors-api

. $(pipenv --venv)/bin/activate

python server.py
