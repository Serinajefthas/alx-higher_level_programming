#!/usr/bin/python3
# script to display value X-Request-Id var in header response
import urllib.request
import sys


if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.headers.get('X-Request-Id')
    print('{}'.format(x_request_id))
