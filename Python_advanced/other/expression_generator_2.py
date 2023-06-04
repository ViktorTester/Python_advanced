"""A generator expression that generates a tuple consisting of two elements:
the name of the day of the week and the number of the day in 2022.
For the first 77 days of the year."""

week = ['Saturday', 'Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', ]
days = ((i, j) for i, j in enumerate(week * 11, start=1))

for x in days:
    print(x)
