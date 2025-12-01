#!/usr/bin/python3
"""
This script takes in a letter, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as parameter q,
and displays the result based on the JSON response.
"""

import sys
import requests

if __name__ == "__main__":
    # Get the letter from command line arguments, default to ""
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    url = "http://0.0.0.0:5000/search_user"

    try:
        # Send POST request with q as parameter
        response = requests.post(url, data={'q': q})

        # Attempt to parse JSON
        json_data = response.json()

        # Check if JSON is empty
        if not json_data:
            print("No result")
        else:
            # Display id and name
            print(f"[{json_data.get('id')}] {json_data.get('name')}")
    except ValueError:
        # JSON was invalid
        print("Not a valid JSON")
