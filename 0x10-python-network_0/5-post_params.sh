#!/bin/bash
#send url
curl -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" -i -s "$1"
