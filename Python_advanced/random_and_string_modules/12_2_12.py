from random import choice

names = [input() for i in range(int(input()))]
names_copy = names.copy()
i = 0

while len(names_copy) > 0:
    x_member = choice(names_copy)
    if x_member != names[i]:
        names[i] += ' - ' + x_member
        names_copy.remove(x_member)
        i += 1

print(*names, sep = '\n')

# The program randomly assigns each student his secret friend,
# who will solve programming problems with him.

# The input to the program in the first line is the number n - the total
# number of students. Next come n lines containing the names and surnames of the students.

# You can't be a secret friend to yourself, and you can't be a secret friend to a few students.