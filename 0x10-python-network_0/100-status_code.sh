#!/bin/bash
#script display only status code of http response
curl -sXL HEAD -w "%{http_code}" "$1"
