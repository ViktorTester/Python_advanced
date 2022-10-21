n = int(input())
matrix = []
unique = []
total = 0
count = 0
counter = 0

for j in range(n):
    matrix.append(input().split())

matrix = [[int(y) for y in x] for x in matrix]

for r in range(n):
    for c in range(n):
        if matrix[r][c] in unique or matrix[r][c] == 0:
            print("NO")
            quit()
        else:
            unique.append(matrix[r][c])

for x in range(n):
    total += matrix[x][0]

for x in range(n):
    count = 0
    for y in range(n):
        count += matrix[x][y]
        if count == total:
            counter += 1
count = 0

for x in range(n):
    count = 0
    for y in range(n):
        count += matrix[y][x]
        if count == total:
            counter += 1
count = 0

for i in range(n):
    count += matrix[i][i]
    if count == total:
        counter += 1
count = 0

for b in range(n):
    count += matrix[b][n - b - 1]
    if count == total:
        counter += 1

if counter == (n * 2 + 2):
    print('YES')
else:
    print("NO")

# A magic square of order n is an n × n square table composed of all numbers 1, 2, 3, . . ,n^2
# so that the sums for each column, each row, and each of the two diagonals are equal.
# The program checks if the given square matrix is a magic square.

# The input to the program is a natural number n — the number of rows and columns in the matrix,
# then the matrix elements: n rows, nn numbers each, separated by spaces.