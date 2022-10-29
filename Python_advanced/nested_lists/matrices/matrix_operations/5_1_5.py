n = int(input())
matrix = []
flag = True

for b in range(n):
    matrix.append(input().split())

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] != matrix[n - y - 1][n - x - 1]:
            flag = False

if flag:
    print("YES")
else:
    print("NO")

# A program for checking the symmetry of a square matrix with respect to the secondary diagonal.

# The input to the program is a natural number n — the number of
# rows and columns in the matrix, then the elements of the matrix.