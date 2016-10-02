import json
import os
from math import sqrt
from sys import argv
from functools import partial


def get_filepath_from_argv(argv):
    filepath = argv[1]
    if not os.path.exists(filepath):
        raise FileExistsError
    return filepath


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_seats_count(bar):
    return bar['Cells']['SeatsCount']


def get_distance(bar, **kwargs):
    longitude1, latitude1 = kwargs['longitude'], kwargs['latitude']
    coordinates = bar['Cells']['geoData']['coordinates']
    longitude2, latitude2 = coordinates[0], coordinates[1]
    return sqrt((longitude1 - longitude2) ** 2 + (latitude1 - latitude2) ** 2)


def get_biggest_bar(data):
    biggest_bar = max(data, key=get_seats_count)
    max_seats_count = biggest_bar['Cells']['SeatsCount']
    # if more than one bar with so many seats
    biggest_bars_list = [bar['Cells']['Name'] for bar in data
                         if get_seats_count(bar) == max_seats_count]
    return biggest_bars_list


def get_smallest_bar(data):
    smallest_bar = min(data, key=get_seats_count)
    min_seats_count = smallest_bar['Cells']['SeatsCount']
    # if more than one bar with so many seats
    smallest_bars_list = [bar['Cells']['Name'] for bar in data
                          if get_seats_count(bar) == min_seats_count]
    return smallest_bars_list


def get_closest_bar(data, longitude, latitude):
    get_distance_to_bar = partial(get_distance, longitude=longitude, latitude=latitude)
    closest_bar = min(data, key=get_distance_to_bar)
    return closest_bar['Cells']['Name']


if __name__ == '__main__':
    try:
        filepath = get_filepath_from_argv(argv)
    except IndexError:
        print('Enter the path to the list of bars by first parameter.')
        exit()
    except FileExistsError:
        print('File does not exists.')
        exit()

    data = load_data(filepath)
    longitude = float(input('Enter the coordinates\nlongitude:'))
    latitude = float(input('latitude:'))

    print('Biggest bar: {}'.format(get_biggest_bar(data)))
    print('Smallest bar: {}'.format(get_smallest_bar(data)))
    print('Closest bar: {}'.format(get_closest_bar(data, longitude, latitude)))
