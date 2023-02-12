countries = ['Russia', 'USA', 'UK', 'Germany', 'France', 'India']
capitals = ['Moscow', 'Washington', 'London', 'Berlin', 'Paris', 'Delhi']
population = [145_934_462, 331_002_651, 80_345_321, 67_886_011, 65_273_511, 1_380_004_385]

for x, y, z in zip(countries, capitals, population):
    print(y, 'is the capital of', x + ', population equal', z, 'people.')

# The program, using parallel iteration through three lists of 'countries',
# 'capitals' and 'population' at once, displays information about each country.
