#!/usr/bin/python3
# script displays body of response (decoded utf-8)
# manages HTTPError exceptions and status codes
import urllib
import sys


if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as response:
            html = response.read().decode('utf-8')
            print(html)
    except urllib.error.HTTPError as e:
        print('Error code: ', e.code)
