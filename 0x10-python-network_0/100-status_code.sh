#!/bin/bash
#send url
curl -s -o /dev/null -w "%{http_code}" "$1" | echo "$(cat)"
