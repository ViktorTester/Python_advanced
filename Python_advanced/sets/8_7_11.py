a, b, c = set(input().split()), set(input().split()), set(input().split())

set_a = a | b | c
set_b = a & b & c
result = set_a - set_b

result = list(result)

for i in range(len(result)):
    result[i] = int(result[i])

result = sorted(set(result))

print(*result)

# There are math grades for three students (on a 10-point scale).
# The program outputs the set of grades that students have,
# except of those that occur in all three students at the same time.