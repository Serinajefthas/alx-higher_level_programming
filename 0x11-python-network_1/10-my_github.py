#!/usr/bin/python3
"""Script takes github username and password and uses github api
to display id"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    url = "https://api.github.com/user"
    r = requests.get(url, auth=HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    json_obj = r.json()
    print(json_obj.get('id'))
