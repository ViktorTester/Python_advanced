with open('population.txt', 'r', encoding='utf-8') as file:
    text = [line.strip().split('\t') for line in file.readlines()]

    for country in text:
        if country[0].startswith('G') and int(country[-1]) > 500_000:
            print(country[0])

# There is a population.txt file with the names of countries and
# their population, separated by the tab character '\t'.

# The program displays all countries whose name begins with the letter 'G'
# and whose population is greater than 500,000 people, without changing their order.