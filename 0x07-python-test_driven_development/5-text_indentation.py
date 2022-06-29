#!/usr/bin/python3

"""
prints a text with 2 new lines after each of these
characters: . ? and :
"""


def text_indentation(text):
    """ checks for characters ., ? and :
    checks if text is string
    returns result """

    new_text = ""

    if type(text) != str:
        raise TypeError("text must be a string")

    if "." not in text and "?" not in text and ":" not in text:
        print("{}".format(text))
    else:
        new_text = text.replace(". ", ".")
        new_text = new_text.replace("? ", "?")
        new_text = new_text.replace(": ", ":")
        new_text = new_text.replace(".", ".\n\n")
        new_text = new_text.replace("?", "?\n\n")
        new_text = new_text.replace(":", ":\n\n")
        " ".join(new_text.split())
        print("{}".format(new_text), sep="", end="")
