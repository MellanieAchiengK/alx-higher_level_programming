#!/usr/bin/python3
""" takes in a URL, sends a request,
displays the value of the X-Request-Id variable found. """

if __name__ == "__main__":
    import requests
    import sys

    output = requests.get(sys.argv[1])
    print(output.headers.get("X-Request-Id"))
