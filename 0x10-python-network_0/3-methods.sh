#!/bin/bash
# Script displays all http methods server accepts
curl -sI -X OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2
