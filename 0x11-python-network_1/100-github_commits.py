#!/usr/bin/python3
import requests
import sys

if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]

    r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(owner, repo))

    commits = r.json()

    for commit in commits[:10]:
        print('{}: {}'.format(commit.get('sha'), commit.get('commit').get('author').get('name')))
