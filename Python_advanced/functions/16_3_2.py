from functools import reduce


def product_of_odds(data):
    filtered = filter(lambda x: x % 2 == 1, data)
    result = reduce(lambda x, y: x * y, filtered, 1)
    return result

# The product_of_odds() function has been rewritten in a functional
# style using the filter() and reduce() built-in functions.

# def product_of_odds(data):  # data -  is a list of integers
#     result = 1
#     for i in data:
#         if i % 2 == 1:
#             result *= i
#     return result
