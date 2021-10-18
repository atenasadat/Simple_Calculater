

def add(a , b):
    """
    This function gets two numbers and returns a+b
    """
    return a+b


def sub(a , b):
    """
    This function gets two numbers and returns a - b
    """
    return a-b


def mul(a , b):
    """
    This function gets two numbers and returns their Multiplication
    """
    return a*b


def dev(a , b):
    """
    This function gets two numbers and returns their division
    """
    if b != 0:
        return a/b
    else:
        print("Divide by zero!")
