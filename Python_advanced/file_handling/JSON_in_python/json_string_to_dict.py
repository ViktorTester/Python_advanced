"""The people variable contains a JSON string containing people's personal information.

The program prints out the person's data according to the following pattern:

<Name>, <Country>, <Age>

It sorts the data by age, and if the age is equal - in alphabetical order."""

import json

people = '[{"name": "Haley Whitney", "country": "British Indian Ocean Territory (Chagos Archipelago)", "age": 54},' \
         '{"name": "Matthew King", "country": "Colombia", "age": 34},' \
         '{"name": "Sean Sullivan", "country": "Mayotte", "age": 40},' \
         '{"name": "Christian Crawford", "country": "Russian Federation", "age": 29},' \
         '{"name": "Sarah Contreras", "country": "Honduras", "age": 82},' \
         '{"name": "Danielle Williams", "country": "Togo", "age": 91},' \
         '{"name": "Jonathan Wilson", "country": "Tunisia", "age": 49},' \
         '{"name": "Patricia Wilkerson", "country": "Georgia", "age": 22},' \
         '{"name": "Zachary Scott", "country": "Brunei Darussalam", "age": 55},' \
         '{"name": "Elizabeth Sanchez", "country": "Nauru", "age": 23},' \
         '{"name": "Jerry Morrow", "country": "San Marino", "age": 23}]'

data = json.loads(people)

for i in sorted(data, key=lambda x: (x["age"], x["name"])):
    print(f'{i["name"]}, {i["country"]}, {i["age"]}')
