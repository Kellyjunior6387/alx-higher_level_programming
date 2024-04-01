#!/bin/bash
#send url and print url
echo "$(curl -sI "$1" | grep -i content-length | awk '{print $2}')"