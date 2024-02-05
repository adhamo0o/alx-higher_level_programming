#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        for element in my_list:
            print(element, end=" ")
            element += 1
    except:
        pass
    return x
