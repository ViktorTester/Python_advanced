n, m = int(input()), int(input())
matrix = []
arr = []

for j in range(n):
    matrix.append(input().split())

matrix = [[int(y) for y in x] for x in matrix]

for a in range(n):
    arr.append(max(matrix[a]))

max_el = max(arr)
max_row = arr.index(max_el)
largest = matrix[max_row].index(max_el)

print(max_row, largest)

# The program receives two natural numbers n and m — the number of rows and
# columns in the matrix, then n rows of m integers each, separated by a space character.

# The program finds the indices (row and column) of the first occurrence of the maximum element.