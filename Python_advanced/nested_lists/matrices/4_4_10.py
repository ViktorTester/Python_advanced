n = int(input())
matrix = []
total = 0

for j in range(n):
    matrix.append(input().split())

matrix = [[int(y) for y in x] for x in matrix]

for i in range(n):
    total += (matrix[i][i])

print(total)

# improved

matrix = []
total = 0

for i in range(n := int(input())):
    row = list(map(int, input().split()))
    matrix.append(row)

for x in range(n):
    total += matrix[x][x]

print(total)

# The trace of a square matrix is the sum of the elements of the main diagonal.
# The program prints the trace of the given square matrix.