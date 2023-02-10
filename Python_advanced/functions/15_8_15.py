colors = input().split()

result = list(map(lambda x: -int(x) + 255, colors))

print(*result)

# In the RGB color scheme, colors are specified using three components:

# R is the intensity of the red component of the color;
# G is the intensity of the green component of the color;
# B is the intensity of the blue component of the color.

# Opposite colors are specified as RGB and (255-R)(255-G)(255-B).
# It is believed that such colors harmonize well with each other.

# The program finds the components of the opposite color according to the three components of the given color.