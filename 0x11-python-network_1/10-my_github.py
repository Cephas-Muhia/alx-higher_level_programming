#!/usr/bin/python3
""" uses the github API to display a github ID based on given credentials.
Usage:./10-my_github.py <GitHub username> <GitHub password>
-Uses basic authentication to access the ID.
"""
import sys
import requests
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    auth = HTTPBasicAuth(sys.argv[1], sys.argv[2])
    r =requests.get("https://api.github.com/user", auth=auth)
    print(r.json().get("id"))

