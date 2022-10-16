year = int(input())

animals = ["Monkey", "Rooster", "Dog", "Pig", "Rat",
            "Bull", "Tiger", "Rabbit", "Dragon", "Snake", "Horse", "Sheep"]

print(animals[year % 12])

# The program reads the year and displays the
# corresponding animal according to the Chinese calendar.