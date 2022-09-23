#!/usr/bin/python3
""" takes in a URL, sends a request, 
displays the value of the X-Request-Id variable found. """

if __name__ == "__main__":
    import urllib.request
    import sys

    with urllib.request.urlopen(sys.argv[1]) as response:
        output = response.info()
        print(output.get("X-Request-Id"))
