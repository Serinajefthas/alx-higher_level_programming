#!/bin/bash
#script displays body of http get request w header variable and value
curl -s "$1" -H "X-School-User-Id: 98"
