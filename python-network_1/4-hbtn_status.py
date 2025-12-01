#!/usr/bin/python3
"""
This script fetches the URL http://0.0.0.0:5050/status
and displays the body of the response as a string.
"""

import requests

url = "http://0.0.0.0:5050/status"

# Send a GET request
response = requests.get(url)

# Get response body as a string
body = response.text

# Display the output in the required format
print("Body response:")
print(f"\t- type: {type(body)}")
print(f"\t- content: {body}")
