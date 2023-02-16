def pretty_print(data, side='-', delimiter='|'):
    s2 = delimiter + " " + f' {delimiter} '.join(map(str, data)) + " " + delimiter
    s = " " + (len(s2) - 2) * side + " "
    print(s)
    print(s2)
    print(s)


pretty_print([1, 2, 10, 23, 123, 3000])
pretty_print(['abc', 'def', 'ghi', '12345'])
pretty_print(['abc', 'def', 'ghi'], side='*')
pretty_print(['abc', 'def', 'ghi'], delimiter='#')
pretty_print(['abc', 'def', 'ghi'], side='*', delimiter='#')

# The pretty_print() function prints the contents of a bordered list.

# The function receives one mandatory data argument as input - a list to be displayed
# and two optional one-character string arguments side and delimiter.

# If the side argument is missing, then side='-',
# and if the delimiter argument is missing, then delimiter='|'.
