is_non_negative_num = lambda x: True if x.replace('.', '', 1).isdigit() else False

print(is_non_negative_num('10.34ab'))
print(is_non_negative_num('10.45'))
print(is_non_negative_num('-18'))
print(is_non_negative_num('-34.67'))
print(is_non_negative_num('987'))
print(is_non_negative_num('abcd'))
print(is_non_negative_num('123.122.12'))
print(is_non_negative_num('123.122'))

# Using the syntax of anonymous functions, I wrote a function 'is_non_negative_num'
# that takes a string argument and returns True if the given argument is a
# non-negative number (integer or real) and False otherwise.