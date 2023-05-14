def list_sum(n: list) -> int:
    """The function returns the sum of the list elements"""
    if not n:
        return 0
    else:
        return n[0] + list_sum(n[1:])


assert list_sum([1, 2, 3]) == 6
assert list_sum([1, 2, 3, 4, 5]) == 15
assert list_sum([0, 0, 0]) == 0
assert list_sum([-1, -2, -3]) == -6
assert list_sum([]) == 0
print('Ok')