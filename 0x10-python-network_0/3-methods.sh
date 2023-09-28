#!/bin/bash
# Script displays all http methods server accepts
curl -sI "$1" | grep "Allow:" | cut -d -f 2 " " 
