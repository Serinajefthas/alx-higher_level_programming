#!/bin/bash
#script displays body of http post request w header variables and value
curl -sX "$1" POST -d "email=test@gmail.com&subject=I will always be here for PLD" 
