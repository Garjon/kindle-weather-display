#!/bin/sh

cd "$(dirname "$0")"

while [ 1 ]
do
    python2 weather-script.py
    rsvg-convert --background-color=white -o weather-script-output.png weather-script-output.svg
    pngcrush -c 0 -ow weather-script-output.png
    cp -f weather-script-output.png /var/data/kindle-image-generator/weather-forecast.png
    sleep 3600
done
