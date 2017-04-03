#!/usr/bin/env python
# -*- coding: utf-8 -*-
# HOMEWORK WEEK 4

# use JSON to examine public data sets, and command line arguments
# to select data subset

import requests
import click


@click.command()
@click.option('--summary/--no-summary', '-s/-no-s', 'summary',
              default=True,
              help='Output summary of weather')
@click.option('--detail/--no-detail', '-d/-no-d', 'detail',
              default=False,
              help='Output weather detail')
@click.option('--temp/--no-temp', '-t/-no-t', 'temp',
              default=True,
              help='Output temperature')
@click.option('--pressure/--no-presure', '-p/-no-p', 'pressure',
              default=False,
              help='Output pressure')
@click.option('--humidity/--no-humidity', 'humidity',
              default=False,
              help='Output humidity')
@click.option('--range/--no-range', '-r/-no-r', 'temprange',
              default=False,
              help='Output temperature high and low')
@click.option('--wind/--no-wind', '-w/-no-w', 'wind',
              default=False,
              help='Output wind speed (and direction, if known)')
@click.argument('place', metavar='city')
def cli(place, summary, detail, temp, pressure, humidity, temprange, wind):
    """
    Weather app using Open Weather Map

    This app provides a weather report for  <city>.

    If the city name contains spaces, surround with quotes, e.g. 'High Wickham'

    If the city name is not unique, add country two letter name after the city
    name (seperated by a comma but no space), e.g. 'London,UK'
    """
    click.echo('Welcome to the weather app')
    args = {}
    args['place'] = place
    args['summary'] = summary
    args['detail'] = detail
    args['temp'] = temp
    args['pressure'] = pressure
    args['humidity'] = humidity
    args['temprange'] = temprange
    args['wind'] = wind
    main(args)


# build the data query - could consider making these arguments :-)
def checkweather(key, args):
    queryurl = 'http://api.openweathermap.org/data/2.5/weather'
    querytype = 'q'
    city = args['place']
    query = city + "&format=json" + "&units=metric"
    apikey = "appid=" + key
    querystring = queryurl + "?" + querytype + "=" + query + "&" + apikey
    # raise query and convert to dictionary using JSON
    response = requests.get(querystring).json()
    return response


def reportweather(weather, args):
    print('Weather report for: {} (closest to {} with weather info).'
          .format(weather['name'], args['place']))
    if args['summary']:
        print('Summary: {}.'.format(weather['weather'][0]['main']))
    if args['detail']:
        print('Detail: {}.'.format(weather['weather'][0]['description']))
    if args['temp']:
        print('Temperature: {} centigrade.'.format(weather['main']['temp']))
    if args['pressure']:
        print('Pressure: {}.'.format(weather['main']['pressure']))
    if args['humidity']:
        print('Humidity: {}.'.format(weather['main']['humidity']))
    if args['temprange']:
        print('Temperature low/high temperature: {}, {} centigrade.'
              .format(weather['main']['temp_min'],
                      weather['main']['temp_max']))
    if args['wind']:
        print('Wind speed: {} km/h.'
              .format(weather['wind']['speed']))
        if 'deg' in weather['wind']:
            print('Wind direction: {} degrees.'
                  .format(weather['wind']['deg']))


def getkey():
    owmkeyfile = "owm.key"
    err = 0

    try:
        with open(owmkeyfile, 'r') as f:
            key = f.readline()
            if key[-1] == "\n":
                key = key[:-1]
    except IOError as err:
        key = "Problem reading OWM api key file '{}'.".format(owmkeyfile)

    return key, err


def main(args):
    key, err = getkey()
    if key and not err:
        weather = checkweather(key, args)
        reportweather(weather, args)
    else:
        print(key)
        print("Unable to obtain weather report. Sorry.")

if __name__ == '__main__':
    cli()
