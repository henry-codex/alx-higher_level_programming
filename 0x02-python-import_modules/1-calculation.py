#!/usr/bin/python3

if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    a = 10
    b = 5
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b))) # Print result of addition
    print("{:d} - {:d} = {:d}".format(a, b, sub(a, b))) # Print result of subtraction
    print("{:d} * {:d} = {:d}".format(a, b, mul(a, b))) # Print result of multiplication
    print("{:d} / {:d} = {:d}".format(a, b, div(a, b))) # Print result of division

