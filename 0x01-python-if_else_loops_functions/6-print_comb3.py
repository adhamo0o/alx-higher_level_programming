#!/usr/bin/python3
for i in range(10):
    for x in range(i + 1, 10):
        if (i, x) != (8, 9):
            print("{:d}{:d}, " .format(i, x), end="")
print("89")
