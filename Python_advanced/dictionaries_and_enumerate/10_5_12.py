words = ['hello', 'bye', 'yes', 'no', 'python', 'apple', 'maybe', 'stepik', 'beegeek']

arr = []
arr2 = []
for i in range(len(words)):
    arr = []
    for j in range(len(words[i])):
        arr.append(ord(words[i][j]))
    arr2.append(arr)

result = dict(zip(words, arr2))

# Can be replaced with the following code:

result = {word: [ord(letter) for letter in word] for word in words}

print(result)

# Using the generator, the program outputs the 'result' dictionary, in which the key
# is a string - an element of the 'words' list, and the value - a list of
# the corresponding ASCII codes of characters of the given string.
