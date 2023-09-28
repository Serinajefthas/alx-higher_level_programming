#!/bin/bash
# Script displays all http methods server accepts
curl -s -I -X OPTIONS "$1" | grep "Allow:" | cut -d" " -f2-
