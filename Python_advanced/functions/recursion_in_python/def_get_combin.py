def ackermann(m: int, n: int) -> int:
    """The ackermann function"""
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ackermann(m - 1, 1)
    return ackermann(m - 1, ackermann(m, n - 1))

assert ackermann(3, 2) == 29
assert ackermann(3, 0) == 5
assert ackermann(1, 0) == 2
assert ackermann(3, 5) == 253
print('Ok')