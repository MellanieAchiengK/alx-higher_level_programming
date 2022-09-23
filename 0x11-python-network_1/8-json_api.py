#!/usr/bin/python3
"""  takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter """

if __name__ == "__main__":
    import requests
    import sys

    if len(sys.argv) < 2:
        q = ""
    else:
        q = sys.argv[1]

    try:
        output = requests.post("http://0.0.0.0:5000/search_user",
                               value=({'q': q}))
        j_result = output.json()

        if j_result:
            print("[{}].{}".format(j_result['id'], j_result['name']))
        else:
            print("No result")

    except ValueError:
        print("Not a valid JSON")
