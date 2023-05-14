#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    list_tup = []
    for indx in range(0, 2):
        try:
            valuea = tuple_a[indx]
        except IndexError:
            valuea = 0
        try:
            valueb = tuple_b[indx]
        except IndexError:
            valueb = 0
        list_tup.append(valuea + valueb)
    return tuple(list_tup)
