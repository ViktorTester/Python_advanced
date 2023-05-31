"""The json file contains information about several groups of people,
and each group has its own identifier.

The program finds the ID of the group that contains the largest
number of women born after 1977.
As an answer, the group identifier and the number of
women separated by a space are displayed."""

import json


def group_people(file_name: str):
    with open(file_name, encoding='utf-8') as file:
        data = json.load(file)

    ages = []

    for i in data:
        total = 0
        for j in i['people']:
            if j['gender'] == 'Female' and j['year'] > 1977:
                total += 1
        ages.append(total)

    ids = [x['id_group'] for x in data]

    max_ages, group_id = 0, 0

    for key, value in dict(zip(ids, ages)).items():
        if value > max_ages:
            max_ages = value
            group_id = key

    print(group_id, max_ages)


group_people(input())
