#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    result = ()
    tuple_a1 = tuple_a + (0, 0)
    tuple_b1 = tuple_b + (0, 0)
    result = tuple_a1[0] + tuple_b1[0], tuple_a1[1] + tuple_b1[1]
    return result
