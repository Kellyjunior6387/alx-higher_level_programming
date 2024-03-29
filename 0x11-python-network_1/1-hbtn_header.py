#!/usr/bin/python3
import urllib.request
import sys
if __name__ == "__main__":

    url = sys.argv[1]

    with urllib.request.urlopen(url) as response:
        if 'X-Request-Id' in response.headers:
            print(response.headers['X-Request-Id'])
        else:
            print("Header not found in the response")