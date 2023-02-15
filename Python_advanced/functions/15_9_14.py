n = int(input())

arr = []
arr1 = []

for i in range(n):
    k = int(input())
    arr = []
    arr1.append(arr)
    for j in range(k):
        s = input()
        arr.append(s[-1])

result = all(map(lambda x: '5' in x, arr1))

print('YES' if result else 'NO')

# The teacher, when checking the work, decided to make sure that in
# each class there is at least one student with a grade of 5 on the test.

# The input to the program is a natural number n - the number of classes.
# Then, for each class, a block of information is entered:

# a natural number k is the number of students in the class;
# then k lines of the form are entered: last name score.

# The program prints YES if there is at least one A student in each class, and NO otherwise.