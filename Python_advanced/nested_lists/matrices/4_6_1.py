num = input().split()
matrix = []
arr = []
n = int(num[0])
m = int(num[1])


if m != 1:
    for j in range(n):
        matrix = []
        for i in range(m):
            if i % 2 == 1:
                matrix.append('*')
            else:
                matrix.append('.')
        arr.append(matrix)
else:
    for k in range(n):
        matrix = []
        if k % 2 == 1:
            matrix.append('*')
        else:
            matrix.append('.')
        arr.append(matrix)

for p in range(len(arr)):
    if p % 2 == 1:
        arr[p].reverse()

for x in range(len(arr)):
    for y in range(len(arr[x])):
        print(arr[x][y], end=' ')
    print()

# The program receives two natural numbers n and m as input. The program creates
# an n × m matrix by filling it with '.' and '*' in staggered order.
# There should be a dot in the upper left corner.

# The input to the program on one line is two natural numbers
# n and m — the number of rows and columns in the matrix.