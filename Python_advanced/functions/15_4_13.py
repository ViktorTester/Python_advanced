athletes = [('Дима', 10, 130, 35), ('Тимур', 11, 135, 39), ('Руслан', 9, 140, 33), ('Рустам', 10, 128, 30),
            ('Амир', 16, 170, 70), ('Рома', 16, 188, 100), ('Матвей', 17, 168, 68), ('Петя', 15, 190, 90)]


def sport(athlete):
    return athlete[n - 1]


n = int(input())

athletes = sorted(athletes, key=sport)

for i in range(len(athletes)):
    print(*athletes[i])

# The athletes list contains information about athletes in the form of tuples: (name, age, height, weight).

# The program sorts the list of athletes by the specified field:

# 1: by name;
# 2: by age;
# 3: by height;
# 4: by weight.
