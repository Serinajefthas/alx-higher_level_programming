#!/bin/bash
#script displays body of json post http response
curl -s "$1 -d "@$2" -X POST -H "Content-Type: application/json"
