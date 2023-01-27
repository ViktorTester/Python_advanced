from math import *

x, func = int(input()), input()


def pow2(x):
    return x * x


def pow3(x):
    return x * x * x


functions = {'square': pow2, 'cube': pow3, 'root': sqrt, 'modulus': abs, 'sine': sin}

print(functions[func](x))

# The program takes a number and a function name, and outputs the result of applying the function to the given number.

# List of possible functions:

# square: the function takes a number and returns its square;
# cube: the function takes a number and returns its cube;
# root: the function takes a number and returns the square root of that number;
# modulus: the function takes a number and returns its modulus;
# sine: The function takes a number (in radians) and returns the sine of that number.
