#!/usr/bin/python3
"""
This script takes in a URL, sends a GET request to the URL,
and displays the value of the
 X-Request-Id variable found in the response header.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]  # Get URL from command line

    # Send a GET request
    response = requests.get(url)

    # Get the value of the 'X-Request-Id' header
    x_request_id = response.headers.get('X-Request-Id')

    # Print the header value
    print(x_request_id)
