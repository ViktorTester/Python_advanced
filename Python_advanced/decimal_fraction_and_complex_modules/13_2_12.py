from fractions import Fraction

n = int(input())
lst = []

for i in range(1, n - 1):
    for j in range(i + 1, n):
        k = Fraction(i, j)
        if k.numerator + k.denominator == n:
            lst.append(Fraction(i, j))

print(max(lst))

# The input to the program is a natural number n. The program finds the largest regular
# irreducible fraction with the sum of the numerator and denominator equal to n.