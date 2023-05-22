def multiply(value):
    def inner(a):
        return value * a
    return inner


f_2 = multiply(2)
assert f_2(5) == 10
assert f_2(15) == 30

f_3 = multiply(3)
assert f_3(5) == 15
assert f_3(15) == 45
print('ok')

# The multiply function takes one argument. The function remembers this value,
# and returns the result of multiplying this number with the value passed again