#!/usr/bin/python3
# script displays body of response(in utf-8) of POST request to url
# w email as param
import urllib.request
import urllib.parse
import sys


if __name__ == "__main__":
    data = urllib.parse.urlencode({"email": sys.argv[2]})
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)

    with urllib.request.urlopen(req) as response:
        response_email = response.read().decode('utf-8')
        print('Your email is: ', response_email)
