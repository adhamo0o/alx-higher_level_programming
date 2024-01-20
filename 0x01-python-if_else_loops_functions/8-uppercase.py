#!/usr/bin/python3
def uppercase(str):
    if ord(str) >= 97 and ord(str) <= 122:
        new_str = str - 32
        print("{new_str:c}".format(new_str))
print("")
