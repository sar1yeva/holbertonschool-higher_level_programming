#!/usr/bin/python3
import urllib.request
'''fetches https://intranet.hbtn.io/status'''
url = "https://intranet.hbtn.io/status"
with urllib.request.urlopen(url) as response:
    data = response.read()
    print(data)
