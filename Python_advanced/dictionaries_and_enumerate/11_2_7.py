data = {}

for _ in range(int(input())):
    name, product, count = input().split()
    data.setdefault(name, {})
    data[name][product] = data[name].get(product, 0) + int(count)

for person, products in sorted(data.items()):
    print(f'{person}:')
    for product, count in sorted(products.items()):
        print(product, count)

# A program for counting the number of units of each type of
# product purchased by each customer of an online store.

# The input to the program is the number n — the number of rows in the online store's
# sales database. This is followed by n lines with records of the type buyer product
# quantity, where buyer is the name of the buyer (string without spaces),
# product is the name of the product (string without spaces),
# quantity is the number of purchased units of the product (natural number).

# The program outputs a list of all customers in lexicographical order,
# followed by a colon after each customer's name, then a list of the names of all the
# items they purchased in lexicographical order, followed by the number of units of
# the item after each item name. Information about each product is displayed on a separate line.