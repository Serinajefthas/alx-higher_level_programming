#!/usr/bin/python3
""" Script displays value of http response header variable"""
import requests
import sys


if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    x_request_id = r.headers.get('X-Request-Id')
    print(x_request_id)
