"""The add_args decorator adds two more values to the passed arguments:
the string 'begin' at the beginning of the arguments and the string 'end'
at the end. The decorator also retains the original name of
the function being decorated and its docstring."""

from functools import wraps


def add_args(func):
    @wraps(func)
    def inner(*args, **kwargs):
        return func('begin', *args, 'end')

    return inner


@add_args
def concatenate(*args):
    """
    Returns the concatenation of the given strings
    """
    return ', '.join(args)


@add_args
def find_max_word(*args):
    """
    Returns the maximum length word
    """
    return max(args, key=len)


assert concatenate('hello', 'world', 'my', 'name is', 'Artem') == 'begin, hello, world, my, name is, Artem, end'
assert concatenate('my', 'name is', 'Artem') == 'begin, my, name is, Artem, end'
assert concatenate.__name__ == 'concatenate'
assert concatenate.__doc__.strip() == """Returns the concatenation of the given strings"""
assert find_max_word('my') == 'begin'
assert find_max_word('my', 'how') == 'begin'
assert find_max_word('my', 'how', 'maximum') == 'maximum'
assert find_max_word.__name__ == 'find_max_word'
assert find_max_word.__doc__.strip() == """Returns the maximum length word"""
print('ok')
