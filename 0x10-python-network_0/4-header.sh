#!/bin/bash
#Send a url

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

curl -X GET -H "X-School-User-Id: 98" -i -s "$1"
