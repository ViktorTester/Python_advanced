n = int(input())
a = set(input())

for i in range(1, n):
    b = set(input())
    a &= b

print(*(sorted(a)))

# The input to the program is a natural number n, and then n different natural numbers,
# each on a separate line. The program displays all
# common digits in ascending order for all entered numbers.