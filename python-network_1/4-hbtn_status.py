#!/usr/bin/python3
"""
This script fetches the URL https://intranet.hbtn.io/status
and displays the body of the response with type, raw bytes,
and UTF-8 decoded content.
"""

import requests

url = "https://intranet.hbtn.io/status"

# Send a GET request and handle the response
response = requests.get(url)

# Ensure the request was successful
response.raise_for_status()  # Will raise an HTTPError if the request failed

body_bytes = response.content  # Raw bytes of the response

print("Body response:")
print(f"\t- type: {type(body_bytes)}")
print(f"\t- content: {body_bytes}")
print(f"\t- utf8 content: {body_bytes.decode('utf-8')}")
