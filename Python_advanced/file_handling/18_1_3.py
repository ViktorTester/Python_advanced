with open('grades.txt', encoding='utf-8') as file:
    text = [line.split() for line in file.readlines()]

    total = 0

    for i in text:
        if int(i[1]) >= 65 and int(i[2]) >= 65 and int(i[3]) >= 65:
            total += 1

    print(total)

# There is a grades.txt text file containing a student’s estimates for three tests
# in each of the trimesters. The lines of the file have the form:
# surname grade_1 grade_2 grade_3.

# The program calculates the number of students who have passed all three tests.
# The test is considered to be passed if the number of points on it is at least 65.
