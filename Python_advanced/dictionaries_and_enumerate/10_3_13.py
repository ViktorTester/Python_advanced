s = 'orange strawberry barley gooseberry apple apricot barley currant orange melon' \
    'pomegranate banana banana orange barley apricot plum grapefruit banana quince' \
    'strawberry barley grapefruit banana grapes melon strawberry apricot currant' \
    'currant gooseberry raspberry apricot currant orange lime quince grapefruit' \
    'barley banana melon pomegranate barley banana orange barley apricot plum banana' \
    'quince lime grapefruit strawberry gooseberry apple barley apricot currant orange' \
    'melon pomegranate banana banana orange apricot barley plum banana grapefruit banana' \
    'quince currant orange melon pomegranate barley plum' \
    'banana quince barley lime grapefruit pomegranate barley'

arr = s.split()
result = {}
for x in arr:
    result[x] = result.get(x, 0) + 1

arr = []
length = 0
for key, value in result.items():
    if value > length:
        length = value
        longest_word = key
    elif length == value:
        arr.append(key)
arr.append(longest_word)

print(min(arr))

# The program outputs the most frequently occurring word of the string s.
# If there are several such words, the one that is less in lexicographic order is displayed.