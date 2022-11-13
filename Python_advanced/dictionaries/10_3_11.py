dict1 = {'a': 100, 'z': 333, 'b': 200, 'c': 300, 'd': 45, 'e': 98, 't': 76, 'q': 34, 'f': 90, 'm': 230}
dict2 = {'a': 300, 'b': 200, 'd': 400, 't': 777, 'c': 12, 'p': 123, 'w': 111, 'z': 666}

result = dict2.copy()

for i, j in dict1.items():
    result[i] = result.get(i, 0) + j

print(result)

# The program combines the contents of two dictionaries dict1 and dict2 by keys,
# adding the values by the same key, if the key is present in both dictionaries.