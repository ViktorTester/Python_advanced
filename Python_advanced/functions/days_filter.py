"""The program filters the days list so that it only contains days
whose names are four characters long or start with the letter 'S'."""

days = ['One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
        'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve']

result = list(filter(lambda s: len(s) == 4 or s.startswith('S'), days))

for i in sorted(result):
    print(i)
