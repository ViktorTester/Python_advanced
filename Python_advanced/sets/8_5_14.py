s = input().split()

for i in range(len(s)):
    s[i] = int(s[i].lstrip('0'))

new_set = set()

for j in range(len(s)):
    if s[j] in new_set:
        print('YES')
    else:
        print('NO')
        new_set.add(s[j])

# The input to the program is a text string containing numbers. For each number,
# the word YES is displayed (in a separate line) if
# this number has previously occurred in the sequence, or NO if it has not.

# Leading zeros in numbers should be ignored.