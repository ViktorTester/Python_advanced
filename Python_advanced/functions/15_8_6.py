func = lambda word: True if word[-1].lower() == 'a' and word[0].lower() == 'a' else False

print(func('abcd'))
print(func('bcda'))
print(func('abcda'))
print(func('Abcd'))
print(func('bcdA'))
print(func('abcdA'))

# Using the syntax of anonymous functions, I wrote a func function that takes a string
# argument and returns True if the passed argument starts and ends
# with the English letter a (case-insensitive) and False otherwise.
