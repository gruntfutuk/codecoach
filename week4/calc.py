#!/usr/bin/env python

# week 4

# functions


def calc(a, b, c='+'):
    if c == '+':
        x = a + b
    elif c == '-':
        x = a - b
    elif c == '-':
        x = a - b
    elif c == '*':
        x = a * b
    elif c == '/':
        x = a / b
    else:
        return "Don't know what you mean"
    return x

print(calc(100, 500))       # uses default operator
print(calc(500, 4, '+'))
print(calc(500, 4, '-'))
print(calc(500, 4, '*'))
print(calc(500, 4, '/'))
print(calc(500, 4, '%'))    # asks for undefined operator
