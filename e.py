def squared(x):
    """
    Returns x **2
    :param x: int.
    :return: int 累乗
    """
    return x ** 2

print(squared(2))


def print_string(string):
    """
    Prints the string
    :param string: str.
    """
    print(string)

print_string("Testing: 1, 2, 3.")


def add_mult(a,b,c,x=100,z=1000):
    """
    Returns the result of two optional params
    multiplied by the addition of three required params.
    :param a: int.
    :param b: int.
    :param c: int.
    :param x: int.
    :param z: int.
    :return: int.
    """
    return a + b + c * x * z

result = add_mult(10, 15, 25)
print(result)


def divide(x):
    """Returns the result of x/2
    :param x: int.
    :return: int.
    """
    return x / 2


def multiply(x):
    """Returns the result of x * 4
    :param x: int.
    :return: int.
    """
    return x * 4

y = divide(4)
z = multiply(y)

print(z)


def convert(string):
    """Converts passed in str to int.
    :param string: str.
    :return: string converted to int.
    """
    try:
        return float(string)
    except ValueError:
        print("Could not convert the string to a float.")

c = convert("55.0")
print(c)
