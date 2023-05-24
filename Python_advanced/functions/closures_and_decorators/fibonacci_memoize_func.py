from functools import wraps


def memoize(func):
    cache = {}

    @wraps(func)
    def inner(*args):
        if args in cache:
            return cache[args]
        cache[args] = func(*args)
        return cache[args]

    return inner


@memoize
def fibonacci(n):
    """
    Returns the n-th Fibonacci number
    """
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


assert fibonacci(50) == 12586269025
assert fibonacci(60) == 1548008755920
assert fibonacci(70) == 190392490709135
assert fibonacci(80) == 23416728348467685
assert fibonacci(90) == 2880067194370816120
assert fibonacci(100) == 354224848179261915075
assert fibonacci.__name__ == 'fibonacci'
assert fibonacci.__doc__.strip() == 'Returns the n-th Fibonacci number'
print('Good')

# When the fibonacci function is called with a certain input value,
# the memoization logic checks to see if the result has already been calculated
# and stored in the cache. If so, the cached result is returned immediately.
# If not, the fibonacci function will be called to calculate the result,
# and the result will be stored in the cache for future use.

# The memoize decorator, in addition to the above, preserves the original name
# of the function being decorated and its documentation string