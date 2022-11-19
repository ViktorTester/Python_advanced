key = []
value = []

for i in range(int(input())):
    word = input().split(':')
    key.append(word[0].lower())
    value.append(word[1].strip())

meanings = dict(zip(key, value))

for j in range(int(input())):
    s = input().lower()
    final = meanings.get(s, "Not found")
    print(final)

# The first line contains one integer n — the number of words in the dictionary.
# The next n lines contain words and their definitions, separated by a colon
# and a space character. The next line contains an integer m — the number
# of search words whose definition is to be displayed.
# The next m lines contain the words themselves, one per line.

# For each word, regardless of case, if it is present in the dictionary,
# the program displays its definition. If the word is not in the dictionary,
# the program displays "Not found", without quotes.