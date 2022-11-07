a, b, c = input().split(), input().split(), set(input().split())

set_a = set(a + b)
result = c - set_a

result = list(result)

for i in range(len(result)):
    result[i] = int(result[i])

result = sorted(set(result), reverse=True)

print(*result)

# There are grades in physics for three students (on a 10-point scale).
# The program outputs a set of grades for the third student
# that are not found in either the first or the second student.