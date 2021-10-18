import math


def add(a, b):
    """
    This function gets two numbers and returns a+b
    """
    return a + b


def sub(a, b):
    """
    This function gets two numbers and returns a - b
    """
    return a - b


def mul(a, b):
    """
    This function gets two numbers and returns their Multiplication
    """
    return a * b


def divide(a, b):
    """
    This function gets two numbers and returns their division
    """
    if b != 0:
        return a / b
    else:
        print("Divide by zero!")


def sin(a):
    """
    This function gets a numbers and returns it's sin
    """
    return math.sin(a)


def cos(a):
    """
    This function gets a numbers and returns it's cos
    """
    return math.cos(a)


def exp(a):
    """
    This function gets a numbers and returns it's exponential
    """
    return math.exp(a)


def log(a, b):
    """
    This function gets a and returns it's log in the basis of b
    """
    return math.log(a, b)


def factorial(a):
    """
        This function gets a and returns a!
    """
    if a == 0 or a == 1:
        return 1
    if a > 1:
        return factorial(a - 1)
    print("The number must be non-negative!")



def radical(a):
    if a < 0:
        print("The number must be non-negative!")
    else:
        return math.sqrt(a)

