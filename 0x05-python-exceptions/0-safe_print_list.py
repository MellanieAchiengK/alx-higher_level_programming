#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            while count < x:
                print("{}".format(my_list[count]), end='')
                count = count + 1
        except IndexError:
            break
    print()
    return count

