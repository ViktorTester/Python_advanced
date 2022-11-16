pets = [('Hatiko', 'Parker', 'Wilson', 50),
        ('Rusty', 'Josh', 'King', 25),
        ('Fido', 'John', 'Smith', 28),
        ('Butch', 'Jake', 'Smirnoff', 18),
        ('Odi', 'Emma', 'Wright', 18),
        ('Balto', 'Josh', 'King', 25),
        ('Barry', 'Josh', 'King', 25),
        ('Snape', 'Hannah', 'Taylor', 40),
        ('Horry', 'Martha', 'Robinson', 73),
        ('Giro', 'Alex', 'Martinez', 65),
        ('Zooma', 'Simon', 'Nevel', 32),
        ('Lassie', 'Josh', 'King', 25),
        ('Chase', 'Martha', 'Robinson', 73),
        ('Ace', 'Martha', 'Williams', 38),
        ('Rocky', 'Simon', 'Nevel', 32)]

result = {}

for i in range(len(pets)):
        result.setdefault(pets[i][1:4], []).append(pets[i][0])

print(result)

# There is a 'pets' list containing information about dogs and their owners.
# Each element of the list is a tuple of species
# (dog name, owner's first name, owner's last name, owner's age).

# The program enters a dictionary into the 'result' variable,
# in which, for each owner, his dogs are listed. The key of the dictionary
# is a tuple (first name, last name, age of the owner),
# and the value is a list of dog names (preserving the original order).