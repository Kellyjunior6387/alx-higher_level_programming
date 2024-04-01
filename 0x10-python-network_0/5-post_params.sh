#!/bin/bash
#Send a url

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

email="test@gmail.com"
subject="I will always be here for PLD"

curl -X POST -d "email=$email&subject=$subject" -i -s "$1"

