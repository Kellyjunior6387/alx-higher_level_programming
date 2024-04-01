#!/bin/bash
#Send a url
curl -X POST -H "Content-Type: application/json" -d "@$2" -s "$1"