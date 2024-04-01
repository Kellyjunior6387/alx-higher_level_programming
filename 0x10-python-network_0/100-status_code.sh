#!/bin/bash
#Send a url

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 
fi
status_code=$(curl -s -o /dev/null -w "%{http_code}" "$1")

echo "$status_code"
