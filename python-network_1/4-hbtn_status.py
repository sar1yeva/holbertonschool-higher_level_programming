#!/usr/bin/python3
"""
This script fetches the URL https://intranet.hbtn.io/status
and displays the body of the response with type, content in bytes,
and UTF-8 decoded content.
"""

import requests

url = "https://intranet.hbtn.io/status"

# Send a GET request to the URL
response = requests.get(url)

# Get the content as bytes
body_bytes = response.content

# Display the output exactly as requested
print("Body response:")
print(f"\t- type: {type(body_bytes)}")
print(f"\t- content: {body_bytes}")
print(f"\t- utf8 content: {body_bytes.decode('utf-8')}")
