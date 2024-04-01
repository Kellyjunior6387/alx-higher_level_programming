#1/bin/bash

if [ $# -ne 1 ]; then
	echo "Usage: $0 <URL>"
	exit 1
fi

response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [ "$response" -eq 200 ]; then
	curl -s "$1"
else 
	echo "Status code $response received. Body not displayed."
fi
