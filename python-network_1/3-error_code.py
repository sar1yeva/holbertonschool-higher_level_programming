#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the body of the response (decoded in utf-8).
If an HTTPError occurs, it prints: Error code: <status code>.
"""

import sys
import urllib.request
import urllib.error

if __name__ == "__main__":
    url = sys.argv[1]  # Get URL from command line

    try:
        # Send the request and automatically close the connection using 'with'
        with urllib.request.urlopen(url) as response:
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Print the HTTP status code if an error occurs
        print(f"Error code: {e.code}")
