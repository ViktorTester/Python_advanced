a, b, c = set(input().split()), set(input().split()), set(input().split())

new_set = a.intersection(b)
result = new_set.difference(c)

result = list(result)

for i in range(len(result)):
    result[i] = int(result[i])

result = sorted(set(result), reverse=True)

print(*result)

# There are grades in computer science for three students (on a 10-point scale).
# The program displays a set of grades that both the first and second
# students have, but which the third student does not have.