#!/bin/bash

ab -n "$1" -c "$2" -t "$3" -s "$4" http://sensorlog-api:5000/simulator/"$5"
