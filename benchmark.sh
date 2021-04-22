#!/bin/bash

ab -n "$1" -c "$2" http://sensorlog-api:5000/simulator
