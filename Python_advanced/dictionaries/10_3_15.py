s = input().lower().split()

for j in range(len(s)):
    s[j] = s[j].strip('.,!?;-:')

result = {}
for x in s:
    result[x] = result.get(x, 0) + 1

arr = []
length = len(s)
for key, value in result.items():
    if value < length:
        length = value
        shortest_word = value

# for key, value in result.items():
#     if value == shortest_word:
#         arr.append(key)

# same code: ^
arr = [key for key, value in result.items() if value == shortest_word]

print(min(arr))

# The program prints out the word (in lower case) that occurs least often.