months = {1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June',
          7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'}
numbers, year = [], []

for key, value in months.items():
    numbers.append(key)
    year.append(value)

result = dict(zip(year, numbers))

# Can be replaced with the following code:


result = {months[i]: i for i in months}

# Can be replaced with the following code:

result = {v: k for k, v in months.items()}

print(result)

# The program, using the generator, outputs the result dictionary, consisting
# of all elements of the months dictionary in which the key and value are swapped.
