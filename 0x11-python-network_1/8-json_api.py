#!/usr/bin/python3
"""
This script sends a POST request to the URL 'http://0.0.0.0:5000/search_user' with the letter as a parameter (q).
It handles the response and displays the id and name if the response is a valid JSON and not empty.
"""

import sys
import requests

if __name__ == "__main__":
    # Get the letter argument from the command line, or set it to an empty string if not provided
    q = sys.argv[1] if len(sys.argv) > 1 else ""

    # Prepare the parameters to send in the POST request
    data = {"q": q}

    # Send the POST request
    response = requests.post("http://0.0.0.0:5000/search_user", data=data)

    try:
        # Try to parse the response as JSON
        json_response = response.json()

        # Check if the JSON is not empty
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
    except ValueError:
        # If the response is not valid JSON
        print("Not a valid JSON")
