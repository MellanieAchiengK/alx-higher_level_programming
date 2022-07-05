#!/usr/bin/python3
"""
adds all arguments to Python list and saves them to a file
"""

import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    lf = load_from_json_file("add_item.json")
except FileNotFoundError:
    lf = []
for x in range(1, len(sys.argv)):
    lf.append(sys.argv[x])
save_to_json_file(lf, "add_item.json")
