colors = {'c1': 'Red', 'c2': 'Grey', 'c3': None, 'c4': 'Green', 'c5': 'Yellow',
          'c6': 'Pink', 'c7': 'Orange', 'c8': None, 'c9': 'White', 'c10': 'Black',
          'c11': 'Violet', 'c12': 'Gold', 'c13': None, 'c14': 'Amber', 'c15': 'Azure',
          'c16': 'Beige', 'c17': 'Bronze', 'c18': None, 'c19': 'Lilac',
          'c20': 'Pearl', 'c21': None, 'c22': 'Sand', 'c23': None}

selected_keys = [key for key, value in colors.items() if value is not None]

result = {k: colors[k] for k in selected_keys}

print(result)

# The program, using the generator, outputs the 'result' dictionary, consisting
# of all elements of the 'colors' dictionary, except for those whose value is None.
