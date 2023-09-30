#!/usr/bin/python3
"""Script sends post request to url w email as param using request package returns body of reponse"""
import requests
import sys


if __name__ == "__main__":
    params = {'email': sys.argv[2]}
    r = requests.post(sys.argv[1], data=data)
    print(r.text)
