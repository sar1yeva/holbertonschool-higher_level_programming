#!/usr/bin/python3
import urllib.request

# Fetch the URL and display the response type, raw bytes, and UTF-8 content
url = "https://intranet.hbtn.io/status"

with urllib.request.urlopen(url) as response:
    body = response.read()  # Read the response as bytes

    print("Body response:")
    print("\t- type: {}".format(type(body)))
    print("\t- content: {}".format(body))
    print("\t- utf8 content: {}".format(body.decode('utf-8')))
