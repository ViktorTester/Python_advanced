students = {'Timur': (170, 75), 'Ruslan': (180, 105), 'Soltan': (192, 68), 'Roman': (175, 70),
            'Madlen': (160, 50), 'Stefani': (165, 70), 'Tom': (190, 90), 'Jerry': (180, 87),
            'Anna': (172, 67), 'Scott': (168, 78), 'John': (186, 79), 'Alex': (195, 120),
            'Max': (200, 110), 'Barak': (180, 89), 'Donald': (170, 80), 'Rustam': (186, 100),
            'Alice': (159, 59), 'Rita': (170, 80), 'Mary': (175, 69), 'Jane': (190, 80)}

selected_keys = {key for key, value in students.items() if value[0] > 167 and value[1] < 75}

result = {k: students[k] for k in selected_keys}

print(result)

# The 'students' variable holds a dictionary containing information
# about the height (in cm) and weight (in kg) of the students.

# Using the generator, the program outputs the 'result' dictionary,
# consisting of all elements of the 'students' dictionary,
# where the height is greater than 167 cm and the weight is less than 75 kg.
