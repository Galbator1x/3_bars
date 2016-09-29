import json
import os
import sys
from math import sqrt
from sys import argv


def get_filepath_from_argv(argv):
    filepath = None
    try:
        filepath = argv[1]
    except IndexError as error:
        print('Enter the path to the list of bars by first parameter')
        sys.exit()
    else:
        if not os.path.exists(filepath):
            print('File does not exists.')
            sys.exit()
    return filepath


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda x: x['Cells']['SeatsCount'])
    max_seats = biggest_bar['Cells']['SeatsCount']
    return [bar['Cells']['Name'] for bar in data if bar['Cells']['SeatsCount'] == max_seats]


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda x: x['Cells']['SeatsCount'])
    min_seats = smallest_bar['Cells']['SeatsCount']
    return [bar['Cells']['Name'] for bar in data if bar['Cells']['SeatsCount'] == min_seats]


def get_closest_bar(data, longitude, latitude):
    closest_bar = min(data, key=lambda x: sqrt((longitude - x['Cells']['geoData']['coordinates'][0]) ** 2 + (
        latitude - x['Cells']['geoData']['coordinates'][1]) ** 2))
    return closest_bar['Cells']['Name']


if __name__ == '__main__':
    filepath = get_filepath_from_argv(argv)
    data = load_data(filepath)
    longitude = float(input('Enter the coordinates\nlongitude:'))
    latitude = float(input('latitude:'))

    print('Biggest bar: {}'.format(get_biggest_bar(data)))
    print('Smallest bar: {}'.format(get_smallest_bar(data)))
    print('Closest bar: {}'.format(get_closest_bar(data, longitude, latitude)))
