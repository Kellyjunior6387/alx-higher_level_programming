#!/usr/bin/python3
import sys
import urllib.request
import urllib.parse
if __name__ == "__main__":

    url = sys.arg[1]
    value = {'email' : sys.arg[2]}

    data = urllib.parse.urlencode(value).encode('utf-8')

    with urllib.request.urlopen(url, data=data) as response:
        body = response.read().decode('utf-8')
    print(body)
