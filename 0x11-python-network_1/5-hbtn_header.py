#!/usr/bin/python3
"""
This script sends a request to a URL and displays the value of the X-Request-Id
variable in the response header.
"""

import sys
import requests

if __name__ == "__main__":
    # The URL is passed as the first argument
    url = sys.argv[1]
    
    # Send the GET request to the URL
    response = requests.get(url)
    
    # Get the value of 'X-Request-Id' from the response headers
    x_request_id = response.headers.get("X-Request-Id")
    
    # Print the value of 'X-Request-Id'
    print(x_request_id)
