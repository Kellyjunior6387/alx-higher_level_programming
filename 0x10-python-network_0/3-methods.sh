#!/bin/bash
#Send a url

# Check if URL argument is provided
if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

# Send an OPTIONS request to the URL using curl
response=$(curl -s -X OPTIONS -i "$1")

# Extract and display the allowed HTTP methods from the response
allowed_methods=$(echo "$response" | awk '/Allow:/ {print $2}')
echo "$allowed_methods"

