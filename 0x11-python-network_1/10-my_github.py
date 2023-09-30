#!/usr/bin/python3
"""Script takes github username and password and uses github api to display id"""
import requests
import sys


if __name__ == "__main__":
    url = "https://api.github.com/user"
    auth = (sys.argv[1], sys.argv[2])
    r = requests.get(url, auth=auth)
    jsonobj = r.json()
    print(jsonobj.get('id'))
