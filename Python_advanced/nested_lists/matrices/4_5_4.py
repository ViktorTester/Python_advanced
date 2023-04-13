n = int(input())
matrix = []
flag = True

for j in range(n):
    matrix.append(input().split())

for x in range(len(matrix)):
    for y in range(len(matrix[x])):
        if matrix[x][y] != matrix[y][x]:
            flag = False

if flag:
    print("YES")
else:
    print("NO")

##### or:

matrix = []
counter = 0
for i in range(n := int(input())):
    row = list(map(int, input().split()))
    matrix.append(row)

for r in range(n):
    for c in range(n):
        if matrix[r][c] == matrix[c][r] and r != c:
            counter += 1

if counter == (n ** 2 - n):
    print('Yes')
else:
    print('No')

# The program checks the symmetry of a square matrix with respect to the main diagonal.
#
# The input to the program is a natural number n — the number of rows and columns
# in the matrix, then the elements of the matrix line by line, separated by a space.