#1/bin/bash
#Send a url
response=$(curl -s -o /dev/null -w "%{http_code}" "$1")
if [ "$response" -eq 200 ]; then
	curl -s "$1"

