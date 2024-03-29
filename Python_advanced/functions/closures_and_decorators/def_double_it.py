def double_it(func):
    """The double_it decorator returns twice the
    result of calling the decorated function"""

    def inner(*args, **kwargs):
        return func(*args, **kwargs) * 2

    return inner


@double_it
def multiply(num1, num2):
    return num1 * num2


@double_it
def some_func_return(a, b, c):
    return a ** b + c


@double_it
def get_sum(*args):
    return sum(args)


assert multiply(9, 4) == 72
assert multiply(100, 4) == 800

assert get_sum(1, 2, 3, 4, 5) == 30

assert some_func_return(4, 5, 4) == 2056
assert get_sum(14, 51, 34) == 198
assert get_sum(14) == 28
assert get_sum() == 0
assert get_sum(43, 5, 43, 43, 43, 43, 3, 2) == 450
print('Good')