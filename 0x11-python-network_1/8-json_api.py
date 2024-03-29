#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        q = sys.argv[1]
    else:
        q = ""

    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})

    try:
        json_response = r.json()
        if json_response:
            print('[{}] {}'.format(json_response.get('id'), json_response.get('name')))
        else:
            print('No result')
    except ValueError:
        print('Not a valid JSON')
