#!/usr/bin/python3
""" takes in a URL, sends a request to the URL
and displays the body of the response (decoded in utf-8) """

if __name__ == "__main__":
    import requests
    import sys

    output = requests.get(sys.argv[1])
 
    if output.status_code >= 400:
        print("Error code: {}".format(output.status_code))

    else:
        print(output.text)
