#!/usr/bin/python3
def no_c(my_string):
    cutted = ''
    for i in my_string:
        if i == 'c' or i == 'C':
            i = ''
        cutted += i
    return(cutted)
