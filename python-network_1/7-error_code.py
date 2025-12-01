#!/usr/bin/python3
"""
This script takes in a URL, sends a GET request to the URL,
and displays the body of the response. If the HTTP status code
is >= 400, it prints: Error code: <status code>.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]  # Get URL from command line

    # Send a GET request
    response = requests.get(url)

    # Check if status code indicates an error
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
