"""The program receives a json file as input, which contains information
about the sales of managers from one car dealership. The file contains for
each manager a list of cars sold by him, as well as the sale price of each car.

The mvp_seller function finds the best seller and prints first his first name,
then his last name, and then the total amount of his sales"""

import json


def mvp_seller(file_name: str):
    with open(file_name, encoding='utf-8') as file:
        data = json.load(file)

    prices, names = [], []

    for i in data:
        total = 0
        for j in i['cars']:
            total += j['price']
        prices.append(total)

    for l in data:
        arr = []
        for value in l['manager'].values():
            arr.append(value)
        names.append(' '.join(arr))

    max_price, name = 0, ''

    for key, value in dict(zip(names, prices)).items():
        if value > max_price:
            max_price = value
            name = key

    print(name, max_price)


mvp_seller(input())
