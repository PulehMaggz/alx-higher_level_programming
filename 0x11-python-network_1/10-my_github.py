#!/usr/bin/python3
"""
This script takes GitHub username and password (personal access token) as arguments,
and uses the GitHub API to display the user ID.
"""

import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    # Get the username and password (personal access token) from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]

    # Make the API request to GitHub with Basic Authentication
    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(username, password))

    # If the request is successful, print the user ID
    if response.status_code == 200:
        user_data = response.json()
        print(user_data.get("id"))
    else:
        # If there's an error (wrong password, etc.), print None
        print(None)
