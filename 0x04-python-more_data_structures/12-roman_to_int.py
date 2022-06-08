#!/usr/bin/python3
def roman_to_int(roman_string):
    if not roman_string:
        return 0
    if not isinstance(roman_string, str):
        return 0
    if not roman_string.isupper():
        return 0
    num = 0
    dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    for i, j in zip(roman_string, roman_string[1:]):
        if i not in dic.keys():
            return 0
        elif dic[i] >= dic[j]:
            num += dic[i]
        else:
            num -= dic[i]
    num += dic[roman_string[-1]]
    return num
