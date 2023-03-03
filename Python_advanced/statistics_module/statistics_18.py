from statistics import fmean as f
from statistics import median as m


with open('data.csv', encoding='utf-8') as file:
    text = [line.strip().split(',') for line in file.readlines()]
    salary = [int(text[i][4]) for i in range(1, len(text))]
    average = round(f(salary))
    median = round(m(salary))
    sample_range = max(salary) - min(salary)

    print('Average salary =', average)
    print('Median salary =', median)
    print('Sample range =', sample_range)

# There is a data.csv file that contains data on residents working in public
# educational institutions. The first three columns contain the full name,
# the fourth - the region of residence, the fifth - the current salary.
# The program defines the following characteristics:

# average salary
# median salary
# sample range (difference between maximum and minimum wages)