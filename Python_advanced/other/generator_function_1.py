"""The generator function gen_squares takes an argument 'n'
and generates squares of numbers from 1 to n inclusive."""

from typing import Generator


def gen_squares(n: int) -> Generator[int, int, None]:
    for j in list(range(1, n + 1)):
        yield j ** 2


for i in gen_squares(3):
    print(i)
