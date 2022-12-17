from fractions import Fraction

n = int(input())
lst = []

for i in range(1, n):
    for j in range(i + 1, n + 1):
        lst.append(Fraction(i, j))

# lst = [Fraction(i, j) for i in range(1, n) for j in range(i + 1, n + 1)]

final = sorted(set(lst))

print(*final, sep='\n')

# The input to the program is a natural number n. The program prints in ascending order
# all irreducible fractions between 0 and 1 whose denominator does not exceed n.
