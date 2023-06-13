#!/usr/bin/python3
'''
class MyInt that inherits from int:
'''


class MyInt(int):
    def __eq__(self, oper):
        return self.real != oper

    def __ne__(self, oper):
        return self.real == oper
