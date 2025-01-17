#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL, and displays
the body of the response (decoded in utf-8). If an HTTPError exception
is encountered, it prints the error code.
"""

import urllib.request
import urllib.error
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    try:
        # Sending the GET request to the URL using a with statement
        with urllib.request.urlopen(url) as response:
            # Read and decode the body of the response
            body = response.read().decode('utf-8')
            print(body)
    except urllib.error.HTTPError as e:
        # Catch HTTPError and print the error code
        print(f"Error code: {e.code}")
