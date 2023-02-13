abscissas, ordinates, applicates = input().split(), input().split(), input().split()

coords = zip(abscissas, ordinates, applicates)

R = 2

result = all(map(lambda x: (float(x[0]) ** 2) + (float(x[1]) ** 2) + (float(x[2]) ** 2) <= R ** 2, coords))

print(result)

# The program receives three lines of text with real numbers, values of abscissa (x),
# ordinate (y) and applicate (z) of three-dimensional space points as input to the program.
# The program checks the location of all points with the entered coordinates inside
# or on the surface of the ball with the center at the origin and radius R = 2.

# The surface equation of a ball (sphere) is: x ** 2 + y ** 2 + z ** 2 = R ** 2