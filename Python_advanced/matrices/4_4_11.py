def average(avg):
    return sum(matrix[i]) / len(matrix[i])

n = int(input())
matrix = []
counter = 0

for j in range(n):
    matrix.append(input().split())

matrix = [[int(y) for y in x] for x in matrix]

for i in range(len(matrix)):
    for b in range(len(matrix[i])):
        if matrix[i][b] > average(matrix[i]):
            counter += 1
    print(counter)
    counter = 0

# The program outputs the number of square matrix elements in each row that are
# greater than the arithmetic mean of the given row.
