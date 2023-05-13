def double_fact(n: int) -> int:
    """The recursive function takes an integer as input
    and calculates the value of the double factorial"""
    if n == 1:
        return 1
    elif n == 2:
        return 2
    return double_fact(n - 2) * n