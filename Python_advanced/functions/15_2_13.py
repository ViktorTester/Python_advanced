def greet(name, *args):
    if len(args) == 0:
        return f'Hello, {name}!'
    else:
        names = ' and '.join(args)
        return f'Hello, {name} and {names}!'

print(greet('Viktor'))
print(greet('Viktor', 'Alex'))
print(greet('Viktor', 'Alex', 'Nick'))


# The greet() function takes an arbitrary number of name string arguments
# (at least one) and returns a greeting according to the pattern.

# The greet() function takes at least one required argument!