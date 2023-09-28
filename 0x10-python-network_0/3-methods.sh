#!/bin/bash
# Script displays all http methods server accepts
curl -sIX OPTIONS "$1" | grep "Allow:" | cut -d " " -f 2
