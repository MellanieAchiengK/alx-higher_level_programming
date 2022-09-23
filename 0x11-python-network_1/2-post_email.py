#!/usr/bin/python3
""" takes in a URL and an email, sends a POST request
displays body (decoded in utf-8) """

if __name__ == "__main__":
    import urllib.request
    import urllib.parse
    import sys

    value = {'email': sys.argv[2]}
    data = urllib.parse.urlencode(value)
    data = data.encode('ascii')
    req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(req) as response:
        output = response.read().decode("utf-8")
    print(output)
