#!/bin/bash
#script displays body of json post http response
curl -sdH "$1$ "@$2" -X POST -H "Content-Type: application/json"
