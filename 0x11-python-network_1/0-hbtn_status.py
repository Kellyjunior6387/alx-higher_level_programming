#!/usr/bin/python3
from urllib import request, error

"""get https://alx-intranet.hbtn.io/status"""

if __name__ == "__main__":
    url = "https://alx-intranet.hbtn.io/status"
    try:
        with request.urlopen(url) as response:
            response = response.read()
            print("Body response:")
            print("\t- type: {}".format(type(response)))
            print("\t- content: {}".format(response))
            print("\t- utf8 content: {}".format(response.decode('utf-8')))
    except error.URLError:
        print("Cannot connect to https://alx-intranet.hbtn.io/status")
