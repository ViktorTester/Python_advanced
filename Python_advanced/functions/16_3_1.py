def concat(*args, sep=' '):
    args = list(args)
    args = map(lambda x: str(x), args)
    args = sep.join(args)

    return args


print(concat('hello', 'python', 'and', 'stepik'))
print(concat('hello', 'python', 'and', 'stepik', sep='*'))
print(concat('hello', 'python', sep='()()()'))
print(concat('hello', sep='()'))
print(concat(1, 2, 3, 4, 5, 6, 7, 8, 9, sep='$$'))

# The concat() function takes a variable number of arguments and concatenates them into
# a single string separated by a separator (sep). If no separator is specified, it is a space.