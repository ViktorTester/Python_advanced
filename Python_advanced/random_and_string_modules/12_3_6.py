import random

n = 10 ** 6
k = 0
s0 = 16

for _ in range(n):
    x = random.uniform(-2, 2)
    y = random.uniform(-2, 2)

    if x ** 3 + y ** 4 + 2 >= 0 and 3 * x + y ** 2 <= 2:
        k += 1

print((k / n) * s0)

# Using the Monte Carlo method, the program calculates the area
# of a figure defined using the following system of inequalities:

# -2 <= x <= 2
# -2 <= y <= 2
# x ** 3 + y ** 4 + 2 >= 0
# 3 * x + y ** 2 <= 2