#!/usr/bin/python3
"""A script that takes URL and email, and sends a post request"""
import sys
import urllib.parse
import urllib.request


if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')
    req = urllib.request.Request(url,data)
    with urllib.request.urlopen(req) as response:
        print(response.read().decode('utf-8'))
