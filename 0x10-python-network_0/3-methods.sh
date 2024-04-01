#!/bin/bash
#Send a url
echo "$(curl -s -X OPTIONS -i "$1" | awk '/Allow:/ {print $2}')"