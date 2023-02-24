def read_csv():
    with open('data.csv', 'r', encoding='utf-8') as file:
        text_keys = file.readline().strip().split(',')
        text_values = [line.strip().split(',') for line in file.readlines()]

        arr = []

        for i in range(len(text_values)):
            dict1 = dict(zip(text_keys, text_values[i]))
            arr.append(dict1)
        return arr


print(read_csv())

# There is a CSV file data.csv containing information in csv format.
# The read_csv function reads data from this file. It returns a list of dictionaries,
# interpreting the first line as the names of the keys,
# and each subsequent line as the values of those keys.