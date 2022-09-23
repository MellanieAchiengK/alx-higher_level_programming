#!/usr/bin/python3
"""Check status"""
import requests
from requests.auth import HTTPBasicAuth
import sys


if __name__ == "__main__":
    """status"""
    user = str(sys.argv[1])
    password = str(sys.argv[2])
    result = requests.get("https://api.github.com/user",
                          auth=(HTTPBasicAuth(user, password)))

    try:
        data = result.json()
        print(data["id"])
    except Exception:
        print("None")
