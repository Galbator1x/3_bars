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
        print('Введите путь к файлу Бары.json первым параметром')
        sys.exit()
    else:
        if not os.path.exists(filepath):
            print('Файл не существует')
            sys.exit()
    return filepath


def load_data(filepath):
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(data):
    biggest_bars = []
    max_seats = -1
    for bar in data:
        seats_count = bar['Cells']['SeatsCount']
        if seats_count > max_seats:
            max_seats = seats_count
            biggest_bars.clear()
            biggest_bars.append(bar['Cells']['Name'])
        elif seats_count == max_seats:
            biggest_bars.append(bar['Cells']['Name'])
    return biggest_bars


def get_smallest_bar(data):
    smallest_bars = []
    min_seats = 1000000
    for bar in data:
        seats_count = bar['Cells']['SeatsCount']
        if seats_count < min_seats:
            min_seats = seats_count
            smallest_bars.clear()
            smallest_bars.append(bar['Cells']['Name'])
        elif seats_count == min_seats:
            smallest_bars.append(bar['Cells']['Name'])
    return smallest_bars


def get_distance_to_bar(longitude1, longitude2, latitude1, latitude2):
    return sqrt((longitude1 - longitude2) ** 2 + (latitude1 - latitude2) ** 2)


def get_closest_bar(data, longitude, latitude):
    closest_bar = None
    min_distance = 1000000
    for bar in data:
        coordinates = bar['Cells']['geoData']['coordinates']
        longitude2, latitude2 = coordinates[0], coordinates[1]
        distance = get_distance_to_bar(longitude, longitude2, latitude, latitude2)
        if distance < min_distance:
            min_distance = distance
            closest_bar = bar['Cells']['Name']
    return closest_bar


if __name__ == '__main__':
    filepath = get_filepath_from_argv(argv)
    data = load_data(filepath)
    print('Введите координаты.\nlongitude:')
    longitude = float(input())
    print('latitude:')
    latitude = float(input())

    print('Biggest bar: {}'.format(get_biggest_bar(data)))
    print('Smallest bar: {}'.format(get_smallest_bar(data)))
    print('Closest bar: {}'.format(get_closest_bar(data, longitude, latitude)))
