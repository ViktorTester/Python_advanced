m, n = int(input()), int(input())

math_students = {input() for i in range(m)}
info_students = {input() for j in range(n)}

both_courses = math_students & info_students
only_math = math_students - both_courses
only_info = info_students - both_courses
total = len(only_math) + len(only_info)

if total > 0:
    print(total)
else:
    print('NO')

# Every student studying at school studies either mathematics or computer science,
# or both of these subjects. The head of the school has lists of students in each subject.

# The program allows the supervisor to find out how many students are studying only one subject.

# The input to the program in the first two lines are the numbers m and
# n - the number of students studying mathematics and computer science,
# respectively. Then m lines follow — the names of students who study
# mathematics and n lines with the names of students who study computer science.
