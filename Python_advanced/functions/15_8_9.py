words = ['beverage', 'monday', 'abroad', 'bias', 'abuse', 'abolish', 'abuse', 'abuse',
         'bid', 'wednesday', 'able', 'betray', 'accident', 'abduct', 'bigot', 'bet',
         'abandon', 'besides', 'access', 'friday', 'bestow', 'abound', 'absent', 'beware',
         'abundant', 'abnormal', 'aboard', 'about', 'accelerate', 'abort', 'thursday',
         'tuesday', 'sunday', 'berth', 'beyond', 'benevolent', 'abate', 'abide', 'bicycle',
         'beside', 'accept', 'berry', 'bewilder', 'abrupt', 'saturday', 'accessory', 'absorb']

result = sorted(list(filter(lambda word: len(word) == 6, words)))

print(*result)

# The program uses the built-in functions filter() and sorted() to display words
# from the list 'words' that are exactly 6 characters long.
# The words are displayed in alphabetical order on one line, separated by a space character.
# An anonymous function is used as a filtering criterion.
