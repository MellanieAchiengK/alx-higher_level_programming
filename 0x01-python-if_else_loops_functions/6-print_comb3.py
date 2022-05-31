#!/usr/bin/python3
for n in range(0, 9):
    for x in range(1, 10):
        print("{:d}{:d}".format(n, x), end=', ')
        if n == 8 and n == 9 and n == x :
            print("{:d}{:d}".format(n, x))
        
        
