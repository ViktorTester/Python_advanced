def matrix(n=1, m=None, value=0):
    if n == 1 and m is None:
        m = 1
    elif n != 1 and m is None:
        m = n
    return [[value] * m for _ in range(n)]


print(matrix())
print(matrix(3))
print(matrix(3, 5))
print(matrix(4, 5, 7))

# The matrix() function creates, fills and returns a matrix of the given size.
# In this case (depending on the arguments passed), it behaves like this:

# matrix() - returns a 1x1 matrix in which the only number is zero;

# matrix(n) - returns an n × n matrix filled with zeros;

# matrix(n, m) - returns a matrix of n rows and m columns filled with zeros;

# matrix(n, m, value) - returns a matrix of n rows and m columns,
# in which each element is equal to the number value.
