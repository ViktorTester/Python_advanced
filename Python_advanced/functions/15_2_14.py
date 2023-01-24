def print_products(*args):
    arr = [args[i] for i in range(len(args)) if type(args[i]) is str and len(args[i]) > 0]

    if len(arr) == 0:
        print('No products')
    else:
        for j in range(1, len(arr) + 1):
            print(f'{j}) {arr[j - 1]}')


print_products('Bananas', [1, 2], ('Horse',), 'Apples', '', 'Macaronis', 5, True)
print_products([4], {}, 1, 2, {'Dog'}, '')

# The print_products() function takes an arbitrary number of arguments and prints
# a list of products (any non-empty string) like this: <product number>) <product name>
# (numbering of products starts from one).
# If there are no products among the passed arguments, the program displays the text 'No products' .
