#!/usr/bin/python3
# script sends post request w arg letter as param using requests package
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv[1]) == 2:
        q = sys.argv[1]
    else:
        q = ""
    data = {'q': q}
    if r.headers.get('content-type') == 'application/json':
        jsondata = r.json()
        if jsondata:
            id = jsondata.get('id')
            name = jsondata.get('name')
            print('[{}] {}'.format(id, name))
        else:
            print('No result')
    else:
        print('Not a valid JSON')
