#!/usr/bin/python2

# Kindle Weather Display
# Matthew Petroff (http://mpetroff.net/)
# September 2012

from xml.dom import minidom
import datetime
import codecs
import urllib2
import json


#
# Geographic location
#

latitude = -33.37
longitude = 151.37


#
# Download and parse weather data
#

icon_map = {
    'chanceflurries': 'shra',
    'chancerain': 'shra',
    'chancesleet': 'shra',
    'chancesnow': 'sn',
    'chancetstorms': 'tsra',
    'clear': 'skc',
    'cloudy': 'ovc',
    'flurries': 'sn',
    'fog': 'mist',
    'hazy': 'mist',
    'mostlycloudy': 'ovc',
    'mostlysunny': 'few',
    'partlycloudy': 'ovc',
    'partlysunny': 'ovc',
    'sleet': 'sn',
    'rain': 'ra',
    'sleet': 'sn',
    'snow': 'sn',
    'sunny': 'skc',
    'tstorms': 'tsra',
    'partlycloudy': 'fg'
}

# Fetch data (change lat and lon to desired location)
weather_json_source = urllib2.urlopen('https://api.wunderground.com/api/810fd352876071d9/conditions/forecast10day/q/' + str(latitude) + ',' + str(longitude) + '.json')
weather_json_string = weather_json_source.read()
parsed_weather_json = json.loads(weather_json_string)

forecasts = parsed_weather_json['forecast']['simpleforecast']['forecastday']
day_one = datetime.datetime.fromtimestamp(int(forecasts[0]['date']['epoch']))
current_temp = str(int(parsed_weather_json['current_observation']['temp_c']))

highs = [None]*4
lows = [None]*4
icons = [None]*4

for i in range(len(forecasts)):
    if (i == 4):
        break

    highs[i] = forecasts[i]['high']['celsius']
    lows[i] = forecasts[i]['low']['celsius']
    icons[i] = icon_map[forecasts[i]['icon']]

weather_json_source.close()


#
# Preprocess SVG
#

# Open SVG to process
output = codecs.open('weather-script-preprocess.svg', 'r', encoding='utf-8').read()

# Insert icons and temperatures
output = output.replace('ICON_ONE',icons[0]).replace('ICON_TWO',icons[1]).replace('ICON_THREE',icons[2]).replace('ICON_FOUR',icons[3])
output = output.replace('CUR_TEMP', str(current_temp)).replace('HIGH_ONE',str(highs[0])).replace('HIGH_TWO',str(highs[1])).replace('HIGH_THREE',str(highs[2])).replace('HIGH_FOUR',str(highs[3]))
output = output.replace('LOW_ONE',str(lows[0])).replace('LOW_TWO',str(lows[1])).replace('LOW_THREE',str(lows[2])).replace('LOW_FOUR',str(lows[3]))

# Insert days of week
one_day = datetime.timedelta(days=1)
days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
output = output.replace('DAY_THREE',days_of_week[(day_one + 2*one_day).weekday()]).replace('DAY_FOUR',days_of_week[(day_one + 3*one_day).weekday()])

# Write output
codecs.open('weather-script-output.svg', 'w', encoding='utf-8').write(output)
