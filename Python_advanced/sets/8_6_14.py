a, b = set(input().split()), set(input().split())
c = a & b
c = list(c)

for i in range(len(c)):
    c[i] = int(c[i])

c = sorted(set(c))

print(*c)

# The input to the program is two lines of text containing numbers.
# The program displays all the numbers in ascending order,
# which are both in the first line and in the second.