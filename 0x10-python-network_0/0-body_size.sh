#!/bin/bash
# Script gets byte size of HTTP response header of URL
curl -s "$1" | wc -c
