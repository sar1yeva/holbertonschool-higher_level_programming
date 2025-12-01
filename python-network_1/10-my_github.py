#!/usr/bin/python3
"""
This script takes your GitHub username and
personal access token (as password),
and uses the GitHub API to display your user ID.
"""

import sys
import requests

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]  # This is your personal access token

    url = "https://api.github.com/user"

    try:
        # Send GET request with Basic Authentication
        response = requests.get(url, auth=(username, password))

# If authentication fails or other error, response.json() may not have 'id'
        if response.status_code == 200:
            user_data = response.json()
            print(user_data.get('id'))
        else:
            print("None")
    except requests.RequestException:
        # Catch connection errors or other request exceptions
        print("None")
