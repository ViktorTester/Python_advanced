key, value = [], []

for i in range(int(input())):
    word = input().split()
    key.append(word[0])
    value.append(word[1])

meanings = dict(zip(key, value))

n = input()

for key, value in meanings.items():
    if key == n:
        print(value)
    elif value == n:
        print(key)

# There is a dictionary consisting of pairs of synonyms. There are no repeated words
# in the dictionary. For one given word, the program determines its synonym.