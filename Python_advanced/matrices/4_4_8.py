n, m = int(input()), int(input())
matrix= []

for _ in range(n * m):
    matrix.append(input())
    if len(matrix) == m:
        print(*matrix)
        matrix.clear()

# The program receives two natural numbers n and m as input, each on a separate
# line — the number of rows and columns in the matrix. Next, the elements of
# the matrix themselves are introduced - words, each on a separate line;
# in a row there are elements first of the first line, then the second, and so on.

# The program first reads the matrix elements one by one, then outputs them as a matrix.