a, b, c = input().split(), input().split(), input().split()

set_a = set(range(11))
set_b = a + b + c

for i in range(len(set_b)):
    set_b[i] = int(set_b[i])

set_b = set(set_b)
result = set_a - set_b
result = sorted(set(result))

print(*result)

# There are grades in biology for three students (ranging from 0 to 10 inclusive).
# The program displays a set of grades that are not found in any of the three students.

