#!/usr/bin/python3
for i in range(122, 97, -1):
    i = i if i % 2 == 0 else i - 32
    print("{:c}".format(i), end="")
