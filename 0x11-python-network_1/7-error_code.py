#!/usr/bin/python3
"""Script that takes in url,sends a url request and displays the body
with the condition
HTTP status code >= 400 brings an error
and the resulting value error is printed """

import sys
import requests

if __name__ == "__main__":
    url = syt.argv[1]

    r = requests.get(url)
    if r.status_code >= 400:
        print("error code: {}".format(r.status_code))
    else:
        print( r.text)

    
                                                                     
