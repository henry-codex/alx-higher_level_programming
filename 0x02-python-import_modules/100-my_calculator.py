#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv
    import calculator_1 as opr
    if not (len(argv) == 4):
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    symb = argv[2]

    ops = {'+': opr.add, '-': opr.sub, '*': opr.mul, '/': opr.div}
    for ind in ops:
        if symb == ind:
            print('{} {} {} = {}'.format(a, symb, b, ops[ind](a, b)))
            exit(0)
    print('Unknown operator. Available operators: +, -, * and /')
    exit(1)
