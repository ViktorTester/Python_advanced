s = input().split()
counter = 0
s_max = 0

for i in range(len(s)):
    s[i] = int(s[i])

for j in range(1, len(s)):
    if s[j] > s[j - 1]:
        s_max = s[j]
        counter += 1

print(counter)

# The input to the program is a text string consisting of natural numbers.
# It forms a list of numbers. The program counts the number of numbers that
# are greater than the number preceding them in this list.