data = [(19542209, 'New York'), (4887871, 'Alabama'), (1420491, 'Hawaii'), (626299, 'Vermont'),
        (1805832, 'West Virginia'), (39865590, 'California'), (11799448, 'Ohio'), (10711908, 'Georgia'),
        (10077331, 'Michigan'), (10439388, 'Virginia'), (7705281, 'Washington'), (7151502, 'Arizona'),
        (7029917, 'Massachusetts'), (6910840, 'Tennessee')]

result = sorted(data, key=lambda x: x[1][-1], reverse=True)

for i in range(len(result)):
    print(result[i][1] + ':', result[i][0])

# The 'data' list contains information about the population of some US states. The program
# sorts the data list in descending order based on the last character in the state name.
# It then prints the elements of this list, each on a new line in city:population format.
