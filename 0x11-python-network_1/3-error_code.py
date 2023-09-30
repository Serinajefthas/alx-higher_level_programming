#!/usr/bin/python3
"""script displays body of response (decoded utf-8)
manages HTTPError exceptions and status codes"""
from urllib import request, error
import sys


if __name__ == "__main__":
    try:
        with request.urlopen(sys.argv[1]) as response:
            print(response.read().decode('utf-8'))
    except error.HTTPError as e:
        print('Error code: ', e.code)
