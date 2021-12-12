"""
Jesko Mueller (c) 2021
ZHAW CCP1-PERF | Performance Analysis Example Lab
x-wing
"""

import random
from urllib import request
from datetime import datetime
import json

import bmemcached

# set client
client = bmemcached.Client(('memcached-server:11211', ))


def get_locations() -> tuple:
    """get historical locations from a study"""
    # animal movement data: https://github.com/movebank/movebank-api-doc/blob/master/movebank-api.md#introduction
    # this is just a set of more or less sensible location data so we don't need to generate new data...
    response = request.urlopen('https://www.movebank.org/movebank/service/public/json?study_id=2911040&'
                                'individual_local_identifiers=1163-1163&sensor_type=gps')
    obj = json.loads(response.read())

    locs = obj['individuals'][0]['locations']
    return (locs, len(locs)) # list of location dicts and length


def set_pos(locs: list, item: int) -> None:
    """set x-wing position with memcached"""
    location = locs[item]
    coord = {'time': datetime.utcfromtimestamp(location['timestamp']/1000).strftime('%Y-%m-%d %H:%M:%S'),
             'long': location['location_long'],
             'lat': location['location_lat']}

    client.set('x-wing-coord', coord, time=2400)
    print(f'X-Wing 0766 currently at {coord}.')



def dog_hack() -> None:
    """Get random dog pic"""
    size = -1
    while not 0 < size < 1000000: # max size of an item in memcached
        req = json.loads(request.urlopen('https://random.dog/woof.json').read())
        size = req['fileSizeBytes']
        dog_url = req['url']
    img = request.urlopen(dog_url).read()

    client.set(dog_url, img, time=2400)
    if random.randint(0, 1000) <= 100:
        print('Hacked some trash in.')


if __name__ == '__main__':
    # get locations
    (locations, length) = get_locations()

    print('Started tracking...')

    # iretate
    cnt = 0 # pylint: disable=invalid-name
    while True:
        set_pos(locations, cnt % length)
        dog_hack()
        cnt = cnt + 1 # pylint: disable=invalid-name
