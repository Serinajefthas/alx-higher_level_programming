#!/bin/bash
#script display only status code of http response
curl -s -L -X HEAD -w "%{http_code}" "$1"
