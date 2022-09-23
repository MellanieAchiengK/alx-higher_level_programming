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
                    value=({'q': q})
        json_result = output.son()
        
        if json_result:
            print("[{}].{}".format(json_result['id'], json_result['name']))
        else:
            print("No result")
    
    except ValueError:
        print("Not a valid JSON")
