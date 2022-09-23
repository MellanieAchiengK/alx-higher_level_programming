#!/usr/bin/python3
""" fetches https://alx-intranet.hbtn.io/status """

if __name__ == "__main__":
    import urllib.request

    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as res:
        output = res.read()
        print("Body response:")
        print("\t- type: {}".format(type(output)))
        print("\t- content: {}".format(output))
        print("\t- utf8 content: {}".format(output.decode('utf-8')))
