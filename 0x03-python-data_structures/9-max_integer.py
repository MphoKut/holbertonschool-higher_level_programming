#!/usr/bin/python3
def max_integer(my_list=[]):
    if not my_list:
        return None

    maxint = sorted(my_list, reverse=True)
    return maxint[0]
