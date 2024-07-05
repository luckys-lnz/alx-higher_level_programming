#!/usr/bin/python3
"""
Takes in url as arg, sends request and recieves a response as the
x-Request-Id found in header response
"""
import sys
import urllib.request

url = sys.argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    print(dict(response.headers).get('X-Request-Id'))
