#!/usr/bin/python3
"""get https://alx-intranet.hbtn.io/status"""
from urllib import request
if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"

    with request.urlopen(url) as response:
        body = response.read().decode('utf-8')

    print("Body response:")
    print("\t- type:", type(body))
    print("\t- content:", body)
     print("\t- utf8 content: {}".format(response.decode('utf-8')))
