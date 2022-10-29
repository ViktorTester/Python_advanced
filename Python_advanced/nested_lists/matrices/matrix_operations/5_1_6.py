import sys

n = int(input())
matrix = []
unique = []
numbers = [i for i in range(1, n + 1)]

for b in range(n):
    matrix.append(input().split())

matrix = [[int(y) for y in x] for x in matrix]

for i in range(n):
    unique.clear()
    for j in range(len(matrix[i])):
        if matrix[i][j] in numbers:
            if matrix[i][j] in unique:
                print('NO')
                sys.exit()
            else:
                unique.append(matrix[i][j])
        else:
            print('NO')
            sys.exit()
unique.clear()

for x in range(n):
    unique.clear()
    for y in range(len(matrix[x])):
        if matrix[y][x] in numbers:
            if matrix[y][x] in unique:
                print('NO')
                sys.exit()
            else:
                unique.append(matrix[y][x])
        else:
            print('NO')
            sys.exit()

print('YES')

# A Latin square of order n is an n × n square matrix, each row and each column
# of which contains all the numbers from 1 to n. The program checks
# if the given square matrix is a Latin square.

# The input program is submitted by a natural number n - the number of lines
# and columns in the matrix, then the elements of the
# matrix: n rows, by n numbers in each, separated by spaces.