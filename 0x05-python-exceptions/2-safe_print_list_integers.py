#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    for i in my_list:
        try:
            while count < x:
                print("{:d}".format(my_list[count]), end='')
                count = count + 1
        except (ValueError, TypeError):
            i = i + 1
            count = count - 1
    print()
    return count


