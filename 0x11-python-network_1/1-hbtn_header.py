#!/usr/bin/python3
"""
Takes in url as arg, sends request and recieves a response as the
x-Request-Id found in header response
"""
import sys
import urllib.request

url = sys.argv[1]
with urllib.request.urlopen(url) as response:
    x_request_id = response.info().get('X-Request-Id')
    print (f"{x_request_id}")
