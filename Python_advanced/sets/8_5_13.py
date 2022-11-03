s = input().lower().split()
new_set = set()

for j in range(len(s)):
    s[j] = s[j].strip('.,!?;-:')

for i in range(len(s)):
    new_set.add(s[i])

print(len(new_set))

# The program determines the total number of distinct words in a line of text, case-insensitive.

# Punctuation marks .,;:-?! are ignored.