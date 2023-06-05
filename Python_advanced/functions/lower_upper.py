"""The program receives English letters separated
by a space in upper or lower case.

The program generates a list of tuples. Each element
of the tuple consists of two values: the corresponding
letter is taken first in uppercase, and then in lowercase."""


def lower_upper(s: str) -> tuple:
    return s.upper(), s.lower()


n = 'T y k P e'.split()

arr = [i for i in map(lower_upper, n)]

print(arr)
