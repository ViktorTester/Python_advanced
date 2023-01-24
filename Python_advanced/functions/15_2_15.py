def info_kwargs(**kwargs):
    for key, value in sorted(kwargs.items()):
        print(key + ':', value)


info_kwargs(first_name='Bill', last_name='Klinton', age=32, job='governor')

# The info_kwargs() function takes an arbitrary number of named arguments and prints
# the named arguments according to the pattern: <argument name>: <argument value>,
# with the argument names in alphabetical order (ascending).