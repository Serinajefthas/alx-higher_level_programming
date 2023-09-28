#!/bin/bash
#script displays body of http get request w header variable and value
curl -sIH "X-School_User_Id: 98" "$1"
