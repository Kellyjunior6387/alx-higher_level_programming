#!/bin/bash
#Send a url

if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

body_size=$(curl -sI "$1" | grep -i content-length | awk '{print $2}')

if [ -z "$body_size" ]; then
	echo "Body size not found"
	exit 1
fi

echo "$body_size"
