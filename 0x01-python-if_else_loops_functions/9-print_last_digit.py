#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        print("{:d}".format(-1 * (number % -10)), end='')
    else:
        print("{:d}".format(number % 10), end='')
        return(number)
    return(-(number % -10))
