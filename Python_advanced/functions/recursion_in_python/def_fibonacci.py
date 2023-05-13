def fib(n: int) -> int:
    """The program displays the N-th Fibonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


print(fib(int(input())))
