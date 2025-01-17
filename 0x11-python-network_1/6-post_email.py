#!/usr/bin/python3
"""
This script sends a POST request to a URL with an email parameter and displays the body of the response.
"""

import sys
import requests

if __name__ == "__main__":
    # Get URL and email address from command-line arguments
    url = sys.argv[1]
    email = sys.argv[2]

    # Create a dictionary to hold the email parameter
    payload = {'email': email}
    
    # Send the POST request
    response = requests.post(url, data=payload)
    
    # Display the body of the response
    print(response.text)
