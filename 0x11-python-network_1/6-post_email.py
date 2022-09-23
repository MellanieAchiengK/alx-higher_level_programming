#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request
displays body (decoded in utf-8) """

if __name__ == "__main__":
    import requests
    import sys

    value = {'email': sys.argv[2]}
    output = requests.post(sys.argv[1], value)
    print(output.text)
