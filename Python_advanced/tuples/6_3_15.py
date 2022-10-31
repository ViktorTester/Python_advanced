n = int(input())

arr = []

f1, f2, f3 = 1, 1, 1
for i in range(n):
    arr.append(f1)
    f1, f2, f3 = f2, f3, f1 + f2 + f3

print(*arr)

# The program reads a natural number n and outputs the first n numbers of the Tribonacci sequence.

# Note. The Tribonacci sequence is a sequence of natural numbers,
# where each subsequent number is the sum of the previous three.