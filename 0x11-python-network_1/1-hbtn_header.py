#!/usr/bin/python3
"""
This script takes in a URL, sends a request to the URL,
and displays the value of the X-Request-Id variable
found in the header of the response.
"""

import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]

    # Send request and handle response using a with statement
    with urllib.request.urlopen(url) as response:
        headers = response.headers
        # Extract and print the X-Request-Id from the headers
        print(headers.get("X-Request-Id"))
