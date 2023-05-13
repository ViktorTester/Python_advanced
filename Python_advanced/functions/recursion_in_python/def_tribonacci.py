def trib(n: int) -> int:
    """The program displays the N-th Tribonacci number."""
    if n == 0:
        return 0
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    return trib(n - 1) + trib(n - 2) + trib(n - 3)


print(trib(int(input())))