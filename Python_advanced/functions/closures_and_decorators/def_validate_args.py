from functools import wraps


def validate_args(func):
    """The decorator validates the passed arguments"""

    @wraps(func)
    def inner(*args, **kwargs):
        if len(args) < 2:
            return 'Not enough arguments'

        if len(args) > 2:
            return "Too many arguments"

        if isinstance(args[0], int) is False or isinstance(args[1], int) is False:
            return 'Wrong types'

        return func(*args)

    return inner


@validate_args
def add_numbers(x, y):
    """Return sum of x and y"""
    return x + y


assert add_numbers(4, 5) == 9
assert add_numbers(4) == 'Not enough arguments'
assert add_numbers() == 'Not enough arguments'
assert add_numbers('hello') == 'Not enough arguments'
assert add_numbers(3, 5, 6) == 'Too many arguments'
assert add_numbers('a', 'b', 'c') == 'Too many arguments'
assert add_numbers(4.5, 5.1) == 'Wrong types'
assert add_numbers('hello', 4) == 'Wrong types'
assert add_numbers(9, 'hello') == 'Wrong types'
assert add_numbers([1, 3], {}) == 'Wrong types'
assert add_numbers.__name__ == 'add_numbers'
assert add_numbers.__doc__.strip() == 'Return sum of x and y'
print('Good')
