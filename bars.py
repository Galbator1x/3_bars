import json
import os
import argparse
from math import sqrt
from functools import partial


def get_filepath_from_argv():
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='path to the list of bars')
    args = parser.parse_args()
    return args.filepath


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
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
    return biggest_bar['Cells']['Name']


def get_smallest_bar(data):
    smallest_bar = min(data, key=get_seats_count)
    return smallest_bar['Cells']['Name']


def get_closest_bar(data, longitude, latitude):
    get_distance_to_bar = partial(get_distance, longitude=longitude, latitude=latitude)
    closest_bar = min(data, key=get_distance_to_bar)
    return closest_bar['Cells']['Name']


if __name__ == '__main__':
    filepath = get_filepath_from_argv()

    data = load_data(filepath)
    if data is None:
        print('File does not exists.')
        exit()
    longitude = float(input('Enter the coordinates\nlongitude: '))
    latitude = float(input('latitude: '))

    print('Biggest bar: {}'.format(get_biggest_bar(data)))
    print('Smallest bar: {}'.format(get_smallest_bar(data)))
    print('Closest bar: {}'.format(get_closest_bar(data, longitude, latitude)))
