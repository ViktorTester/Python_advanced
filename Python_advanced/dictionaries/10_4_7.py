sw = list(input())
key, value = [], []

for i in range(int(input())):
    word = input().lower().split()
    key.append(int(word[1]))
    value.append(word[0].strip(':'))

text = ''.join(sw)
result = {}

for x in sw:
    result[x] = result.get(x, 0) + 1

meanings = dict(zip(key, value))

for i in text:
    print(meanings[result[i]], end='')

# A program for deciphering a secret word using frequency analysis.

# The first line contains the encrypted word. The second line contains a single integer n,
# the number of letters in the dictionary. The following n lines contain how many times
# a particular letter of the alphabet occurs in this word - <letter>: <frequency>.

# It is guaranteed that letter frequencies do not repeat.