"""The generator function gen_fibonacci_numbers takes an argument 'n'
and generates the nth number of Fibonacci numbers."""

from typing import Generator


def gen_fibonacci_numbers(n: int) -> Generator[int, int, None]:
    a, b = 1, 1

    for j in range(n):
        yield a

        a, b = b, a + b


for i in gen_fibonacci_numbers(5):
    print(i)
