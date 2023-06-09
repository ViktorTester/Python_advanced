"""The find_keys function takes an arbitrary number of named arguments
and selects only those parameter names whose values are lists or tuples.
The function collects all the names of such parameters into a list,
sorts them alphabetically regardless of case, and returns them as a result."""


def find_keys(**kwargs) -> list:
    arr = []
    for key, value in kwargs.items():
        if isinstance(value, (list, tuple)):
            arr.append(key)

    return sorted(arr, key=str.lower)


assert find_keys(t=[4, 5], W=[5, 3], A=(3, 2), a={2, 3}, b=[4]) == ['A', 'b', 't', 'W']
assert find_keys(name='Bruce', surname='Wayne') == []
assert find_keys(marks=[4, 5], name='ashle', surname='Brown', age=20, Also=(1, 2)) == ['Also', 'marks']
print('ok')
