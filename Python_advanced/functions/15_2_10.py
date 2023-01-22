def count_args(*args):

    return len(args)

print(count_args())
print(count_args(10))
print(count_args('one', 'two'))
print(count_args([], (''), 'a', 12, False))

# The count_args () function takes an arbitrary number of arguments
# and returns the number of arguments transferred to it.