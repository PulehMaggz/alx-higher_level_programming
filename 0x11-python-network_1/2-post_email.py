#!/usr/bin/python3
"""
This script takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays
the body of the response (decoded in utf-8).
"""

import urllib.parse
import urllib.request
import sys

if __name__ == "__main__":
    url = sys.argv[1]
    email = sys.argv[2]

    # Encode the email as a POST parameter
    data = urllib.parse.urlencode({'email': email}).encode('utf-8')

    # Send the POST request using a with statement
    with urllib.request.urlopen(url, data) as response:
        # Read and decode the response body
        body = response.read().decode('utf-8')
        print(body)

