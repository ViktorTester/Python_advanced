import random

n = 10 ** 6
S = 4
k = 0

for _ in range(n):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        k += 1

print((k / n) * S)

# The program using the Monte Carlo method determines the approximate value of the number π.

# The area of a unit circle, i.e. a circle with a radius equal to R = 1, is S = πR ** 2 = π.

# The unit circle equation is x ** 2 + y ** 2 = 1