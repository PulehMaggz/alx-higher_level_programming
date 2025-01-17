#!/usr/bin/python3
"""
This script fetches https://alx-intranet.hbtn.io/status using the requests package
and displays the body of the response.
"""

import requests

if __name__ == "__main__":
    # Sending the GET request to the URL
    response = requests.get("https://alx-intranet.hbtn.io/status")
    
    # Print the formatted response body
    print("Body response:")
    print(f"    - type: {type(response.text)}")
    print(f"    - content: {response.text}")
