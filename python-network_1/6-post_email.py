#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request to the URL
with the email as a parameter, and displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]       # Get the URL from command line
    email = sys.argv[2]     # Get the email from command line

    # Send a POST request with the email as a parameter
    response = requests.post(url, data={'email': email})

    # Print the body of the response
    print(response.text)
