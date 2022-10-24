num = input().split()
m = int(num[0])
n = int(num[1])
matrix = []
arr = []

for i in range(1, n * m + 1):
    matrix.append(i)
    if len(matrix) == m:
        arr.append(matrix)
        matrix = []

for c in range(m):
    for r in range(n):
        print(str(arr[r][c]).ljust(2), end=' ')
    print()

# The program receives two natural numbers n and m as input. The program creates an
# n × m matrix and fills it with numbers from 1 to n ⋅ m according to the pattern.

# Sample Input 1:
# 3 7

# Sample Output 1:
# 1  4  7  10 13 16 19
# 2  5  8  11 14 17 20
# 3  6  9  12 15 18 21