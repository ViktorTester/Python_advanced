num = input().split()
n = int(num[0])
m = int(num[1])
matrix = []
arr = []

for i in range(1, n * m + 1):
    matrix.append(i)
    if len(matrix) == m:
        arr.append(matrix)
        matrix = []

for p in range(n):
    if p % 2 == 1:
        arr[p].reverse()

for x in range(len(arr)):
    for y in range(len(arr[x])):
        print(str(arr[x][y]).ljust(2), end=' ')
    print()

# The program receives two natural numbers n and m as input.
# The program creates an n × m matrix by filling it with a "snake".