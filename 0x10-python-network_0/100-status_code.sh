#!/bin/bash
#A Bash script that displays the status code of the response URL
curl -s -o /dev/null -w "%{http_code}" "$1"
