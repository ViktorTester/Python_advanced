key, value = [], []

for i in range(int(input())):
    word = input().lower().split()
    key.append(word[0])
    value.append(word[1])

meanings = dict(zip(key, value))

arr = [input().lower() for j in range(int(input()))]

arr2 = []
for x in range(len(arr)):
    arr2.clear()
    for key, value in meanings.items():
        if arr[x] in value:
            arr2.append(key)
    if len(arr2) > 0:
        print(*arr2)
    else:
        print("user not found")

# improved

d = {}
for i in range(int(input())):
    data = input().split()
    if data[1] not in d.keys():
        d[data[1]] = [data[0]]
    else:
        d[data[1]] += [data[0]]

for j in range(int(input())):
    name = input()
    if name in d.keys():
        for key, value in d.items():
            if key == name:
                print(*value)
    else:
        print('user not found')

# The boy wrote down the phone numbers of all his friends
# in order to automate the search for the right number.

# Each of the boy's friends may have one or more phone numbers.
# The program helps the boy find all the numbers of a certain friend.