m, n = int(input()), int(input())

math_and_info = [input() for i in range(m + n)]
set_a = set(math_and_info)

a = len(math_and_info) - len(set_a)

if len(math_and_info) == len(set_a):
    print(m + n)
elif len(math_and_info) / 2 == len(set_a):
    print('NO')
elif a > 0:
    print((m + n) - (a * 2))

# Every student studying at school studies either mathematics or computer science,
# or both of these subjects. The head of the school has lists of students studying
# each subject. By chance, the lists of all students were mixed up.

# The program allows the supervisor to find out how many students study only one subject.

# The input to the program in the first two lines are the numbers
# m and n - the number of students studying mathematics and computer science,
# respectively. Then m + n lines follow — the names
# of students studying mathematics and computer science, in any order.