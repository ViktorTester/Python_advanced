m = int(input())
n = int(input())
first_set = set([input() for _ in range(n)])
empty_set = set()

if m == 1:
    print(*(sorted(first_set)), sep='\n')
else:
    for i in range(m - 1):
        for j in range(int(input())):
            empty_set.add(input())
        first_set.intersection_update(empty_set)
        empty_set.clear()
    first_set = sorted(first_set)
    for row in first_set:
        print(row)

# The head of the school wanted to know which of his students had attended
# all the lessons since the beginning of the school year.
# For each lesson there is a sheet with a list of the students present.

# The program determines the names of the students who were present at all lessons.

# The input to the program in the first line is the number m - the number of lessons
# conducted since the beginning of the school year. Then there are m blocks of lines
# describing sheets with surnames. The first line of each block contains the number
# of surnames n(i), then there are n(i) lines with the surnames of those who attended the i-th lesson.