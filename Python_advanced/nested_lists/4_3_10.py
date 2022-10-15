def pascal(n):
    arr = []

    for i in range(n + 1):
        arr.append([1] * (i + 1))

    if len(arr) >= 3:
        for j in range(2, len(arr)):
            for x in range(1, len(arr[j]) - 1):
                arr[j][x] = arr[j - 1][x - 1] + arr[j - 1][x]
    return arr[-1]

n = int(input())
print(pascal(n))

# Pascal's triangle is an infinite table of binomial coefficients that has a
# triangular shape. In this triangle, there are units at the top and on the sides.
# Each number is equal to the sum of the two numbers above it.

# 0:      1
# 1:     1 1
# 2:    1 2 1
# 3:   1 3 3 1
# 4:  1 4 6 4 1
#       .....

# The number n is given as input to the program. The program returns the specified
# line of Pascal's triangle as a list (line numbering starts from zero).
