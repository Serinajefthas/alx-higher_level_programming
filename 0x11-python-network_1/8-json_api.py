#!/usr/bin/python3
"""script sends post request w arg letter as param using requests package"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        q = ""
    else:
        q = sys.argv[1]
    data = {'q': q}

    r = requests.post("http://0.0.0.0:5000/search_user", data=data)
    try:
        jsondata = r.json()
        if jsondata:
            id = jsondata.get('id')
            name = jsondata.get('name')
            print('[{}] {}'.format(id, name))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
