key, value = [], []

for i in range(int(input())):
    word = input().split()
    key.append(word[0])
    value.append(word[1:])

meanings = dict(zip(key, value))

arr = [input() for j in range(int(input))]

for x in range(len(arr)):
    for key, value in meanings.items():
        if arr[x] in value:
            print(key)

# The input to the program is a list of countries and cities of each country.
# Then the names of the cities are given. The program displays in which country each city is located.