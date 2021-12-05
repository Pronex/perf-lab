#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Jesko Mueller (c) 2021
ZHAW CCP1-PERF | Performance Analysis Example Lab
a-wing
"""

import time
from urllib import request
from datetime import datetime
import json

import bmemcached

# set client
client = bmemcached.Client(('memcached-server:11211', ))

def get_pos() -> dict:
    """get a-wing position"""
    # ISS space station position: http://open-notify.org/Open-Notify-API/ISS-Location-Now/
    response = request.urlopen('http://api.open-notify.org/iss-now.json')
    obj = json.loads(response.read())

    tstamp = datetime.utcfromtimestamp(obj['timestamp']).strftime('%Y-%m-%d %H:%M:%S')

    return {'time': tstamp,
            'long': obj['iss_position']['longitude'],
            'lat': obj['iss_position']['latitude']}


def set_pos() -> dict:
    """set a-wing position with memcached"""
    coord = get_pos()
    client.set('a-wing-coord', coord, time=2)
    print(f'A-Wing 4242 currently at {coord}.')


if __name__ == '__main__':

    print('Started tracking...')

    while True:
        set_pos()
        time.sleep(1)
