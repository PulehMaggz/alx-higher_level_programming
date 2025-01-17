#!/usr/bin/python3
"""
This script sends a request to a URL and displays the body of the response.
If the HTTP status code is greater than or equal to 400, it prints: Error code: followed by the HTTP status code.
"""

import sys
import requests

if __name__ == "__main__":
    url = sys.argv[1]

    # Send the GET request
    response = requests.get(url)

    # Check if the status code is >= 400
    if response.status_code >= 400:
        print(f"Error code: {response.status_code}")
    else:
        print(response.text)
