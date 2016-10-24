# -*- coding: utf-8 -*-
import datetime
import json
import time
import urllib.parse
import urllib.request as urllib2


def request(url):
    req = urllib2.Request(url)
    return json.loads(urllib2.urlopen(req).read().decode())


def location(city):
    params = urllib.parse.urlencode({'address': city,
                                     'sensor': False})
    url = 'http://maps.googleapis.com/maps/api/geocode/json?{}'.format(params)
    return request(url)['results']


def current_time(city):
    try:
        locations = location(city)[0]['geometry']['location']
        params = {'location': str(locations['lat']) + ',' + str(locations['lng']),
                  'timestamp': int(time.time()),
                  'sensor': False}
        url = 'https://maps.googleapis.com/maps/api/timezone/json?{}'.format(urllib.parse.urlencode(params))
        result = request(url)
        local_time = datetime.datetime.utcnow() + datetime.timedelta(seconds=result['rawOffset'])
        return str(local_time)[:-7]
    except IndexError:
        return None

if __name__ == '__main__':
    print(current_time('Чирчик'))
