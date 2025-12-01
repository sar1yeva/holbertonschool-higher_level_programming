#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id
variable found in the header of the response.
"""

import sys
import urllib.request

if __name__ == "__main__":
    # Get the URL from the command line argument
    url = sys.argv[1]

# Send a request to the URL and automatically close the connection using 'with'
    with urllib.request.urlopen(url) as response:
        # Retrieve the value of the 'X-Request-Id' header
        x_request_id = response.headers.get('X-Request-Id')
        print(x_request_id)
