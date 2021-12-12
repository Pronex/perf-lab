"""
Jesko Mueller (c) 2021
ZHAW CCP1-PERF | Performance Analysis Example Lab
a-wing
"""

import time

import bmemcached

# keys to get
KEYS = ['a-wing-coord', 'x-wing-coord']

# set client
client = bmemcached.Client(('memcached-server:11211', ))

def get_coords() -> dict:
    """get ship positions"""
    for item in KEYS:
        res = client.get(item)
        print(f'pos: {item} at {res}')


if __name__ == '__main__':
    while True:
        get_coords()
        time.sleep(1)
