def create_dict():
    d = {}
    i = 0

    def inner(word):
        nonlocal i
        i += 1
        d[i] = word
        return d

    return inner


f_1 = create_dict()
assert f_1('hello') == {1: 'hello'}
assert f_1(100) == {1: 'hello', 2: 100}
assert f_1([1, 2, 3]) == {1: 'hello', 2: 100, 3: [1, 2, 3]}

f_2 = create_dict()
assert f_2('Power') == {1: 'Power'}

print('ok')

# The create_dict closure function. In the form of a dictionary, it stores
# all the values that will be passed to it. The keys of this dictionary
# are natural numbers equal to the number of this function call.