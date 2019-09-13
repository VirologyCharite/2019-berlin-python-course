#!/usr/bin/env python


class FunkyNumbers:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        return self.value + (2 * other.value)

    def __eq__(self, other):
        print("Oh, do I have to? It's Friday.")
        return False


a = FunkyNumbers(3)
b = FunkyNumbers(4)

print(a + b)

if a == b:
    pass
