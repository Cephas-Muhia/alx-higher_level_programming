#!/usr/bin/python3
"""Sends a request to a given URL and displays the response body.
Usage: ./7-error_code.py <URL>
  - Handles HTTP errors.
  """

import sys
import requests

if __name__ == "__main__":
    url = syt.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("error code: {}".format(r.status_code))
    else:
        print( r.text)

    
                                                                     
