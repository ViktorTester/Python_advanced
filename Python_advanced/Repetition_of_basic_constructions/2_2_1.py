first = 0
second = 0
third = 0
forth = 0

n = int(input())

for i in range(n):
    x = input().split()
    a = int(x[0])
    b = int(x[1])
    if a > 0 and b > 0:
        first += 1
    elif a < 0 and b > 0:
        second += 1
    elif a < 0 and b < 0:
        third += 1
    elif a > 0 and b < 0:
        forth += 1

print('First quarter:', first)
print('Second quarter:', second)
print('Third quarter:', third)
print('Forth quarter:', forth)

# The input to the program is string n. Then n-strings consisting of two integers —
# the coordinates of the point. The program counts and displays the number
# of points that lie in each coordinate quarter.