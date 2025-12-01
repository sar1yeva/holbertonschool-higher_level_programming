#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the URL
with the email as a parameter, and displays the body of the response.
"""

import sys
import urllib.request
import urllib.parse

if __name__ == "__main__":
    url = sys.argv[1]       # URL from command line
    email = sys.argv[2]     # Email from command line

    # Encode the email as POST data
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send the POST request using a with statement
    with urllib.request.urlopen(url, data=data) as response:
        # Read and decode the response
        body = response.read().decode('utf-8')
        print(body)
