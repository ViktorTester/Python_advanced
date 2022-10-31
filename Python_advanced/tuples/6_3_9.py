n = int(input())
arr = [input().split() for _ in range(n)]

for i in range(n):
    arr[i][1] = int(arr[i][1])
    print(*arr[i])

for j in range(len(arr)):
    arr[j] = tuple(arr[j])

tpl = tuple(arr)

print()

for x in range(len(tpl)):
    if tpl[x][1] >= 4:
        print(*tpl[x])

# The program displays a list of good and excellent students in the class.

# The program receives a natural number n as input, followed
# by n lines with the student's name and grade on each line.

# The program should first display all the entered strings with the names and
# grades of the students in the same order. This is followed by an empty line,
# and then the lines with the names and grades of good
# and excellent students are displayed (in the same order).

# Solved using tuples.
