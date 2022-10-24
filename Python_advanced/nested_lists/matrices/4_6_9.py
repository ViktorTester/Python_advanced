num = input().split()
n = int(num[0])
m = int(num[1])
matrix = []
arr = []
num = 0

for i in range(1, n * m + 1):
    matrix.append(i)
    if len(matrix) == m:
        arr.append(matrix)
        matrix = []

for q in range(n * m):
    for b in range(len(arr)):
        for h in range(len(arr[b])):
            if b + h == q:
                num +=1
                arr[b][h] = num

for x in range(len(arr)):
    for y in range(len(arr[x])):
        print(str(arr[x][y]).ljust(2), end=' ')
    print()

# The program receives two natural numbers n and m as input.
# The program creates an n×m matrix by filling it with "diagonals" according to the example.

# Sample Input 1:
# 3 5

# Sample Output 1:
# 1  2  4  7  10
# 3  5  8  11 13
# 6  9  12 14 15