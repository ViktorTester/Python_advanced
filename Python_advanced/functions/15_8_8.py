is_num = lambda x: True if '-' not in x[1:] and x.replace('.', '', 1).replace('-', '', 1).isdigit() else False

# Using the syntax of anonymous functions, I wrote an 'is_num' function that takes a string
# argument and returns True if the given argument is a number (integer or real) and False otherwise.