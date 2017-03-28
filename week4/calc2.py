# week 4

# functions alternative calculator function


def add(x, y):
    return x+y


def sub(x, y):
    return x-y


def div(x, y):
    if y != 0:
        return x/y
    return("Divide by zero not allowed.")


def mul(x, y):
    return x*y


def calc(x, y, f=add):
    return f(x, y)

try:
    print(calc(100, 500))
    print(calc(500, 4, add))
    print(calc(500, 4, sub))
    print(calc(500, 4, mul))
    print(calc(500, 4, div))
    print(calc(500, 4, mod))
except NameError:
    print('An unknown function or variable was referenced.')
