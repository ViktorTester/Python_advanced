def create_accumulator(total=0):
    """The closure function sums up all the
    values that will be passed to it."""

    def accumulator(value):
        nonlocal total
        total += value
        return total

    return accumulator


sum_1 = create_accumulator(100)
assert sum_1(1) == 101
assert sum_1(5) == 106
assert sum_1(2) == 108

sum_2 = create_accumulator()
assert sum_2(3) == 3
assert sum_2(4) == 7
print('ok')