#!/bin/bash
#send a url
curl -s -o /dev/null -w "%{http_code}" "$1" | grep -q 200 && curl -s "$1"