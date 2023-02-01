from functools import reduce

data = [['Tokyo', 35676000, 'primary'],
        ['New York', 19354922, 'nan'],
        ['Mexico City', 19028000, 'primary'],
        ['Mumbai', 18978000, 'admin'],
        ['Sao Paulo', 18845000, 'admin'],
        ['Delhi', 15926000, 'admin'],
        ['Shanghai', 14987000, 'admin'],
        ['Kolkata', 14787000, 'admin'],
        ['Los Angeles', 12815475, 'nan'],
        ['Dhaka', 12797394, 'primary'],
        ['Buenos Aires', 12795000, 'primary'],
        ['Karachi', 12130000, 'admin'],
        ['Cairo', 11893000, 'primary'],
        ['Rio de Janeiro', 11748000, 'admin'],
        ['Osaka', 11294000, 'admin'],
        ['Beijing', 11106000, 'primary'],
        ['Manila', 11100000, 'primary'],
        ['Moscow', 10452000, 'primary'],
        ['Istanbul', 10061000, 'admin'],
        ['Paris', 9904000, 'primary']]

filter_result = list(filter(lambda cities: cities[1] > 10 ** 7 and cities[2] == 'primary', data))
map_result = list(map(lambda cities: cities[0], filter_result))
sorted_result = sorted(map_result)
result = reduce(lambda x, y: x + y + ', ', sorted_result, 'Cities: ')

print(result[:-2] + '.')

# The program, using the built-in functions filter(), map(), sorted() and reduce(), displays
# in alphabetical order a list of primary cities with a population of more than 10,000,000 people.
