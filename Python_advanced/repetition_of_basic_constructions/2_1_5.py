s = input().split()
x = ' '.join(s)
counter = 1

for i in range(len(x)):
    if x[i] == ' ':
        counter += 1

print(counter)

# or

print((input().split()))

# Given a string consisting of words separated by spaces.
# The program counts the number of words in this string.